#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const os = require('os');
const readline = require('readline');

// Enable keypress events
readline.emitKeypressEvents(process.stdin);
if (process.stdin.isTTY) {
    process.stdin.setRawMode(true);
}

const HEADER = `
==========================================
    Antigravity Kit Setup by NghiaPT
==========================================
`;

// Paths
const WORKFLOWS_SRC = path.join(__dirname, '..', 'workflows');
const USER_HOME = os.homedir();
const GLOBAL_DEST = path.join(USER_HOME, '.gemini', 'antigravity', 'global_workflows');
const LOCAL_DEST = path.join(process.cwd(), '.agent', 'workflows');

// Menu Options
const OPTIONS = [
    {
        label: 'Install Global (Recommended)',
        action: async () => {
            await installWorkflows(GLOBAL_DEST, 'Global');
            process.exit(0);
        }
    },
    {
        label: 'Install Only on Context Project',
        action: async () => {
            await installWorkflows(LOCAL_DEST, 'Local Project');
            process.exit(0);
        }
    },
    {
        label: 'Exit',
        action: () => process.exit(0)
    }
];

let selectedIndex = 0;

// --- Helper Functions ---

function ensureDirectoryExists(dir) {
    if (!fs.existsSync(dir)) {
        try {
            fs.mkdirSync(dir, { recursive: true });
            // console.log(`Created directory: ${dir}`); // keep output clean
        } catch (err) {
            console.error(`❌ Error creating directory ${dir}: ${err.message}`);
            return false;
        }
    }
    return true;
}

async function installWorkflows(destination, typeLabel) {
    // restore standard input for logging
    // (optional, but raw mode can accept keypress artifacts if we type during async ops)

    console.log(`\n\n[Installing Workflows (${typeLabel})]...`);

    if (!fs.existsSync(WORKFLOWS_SRC)) {
        console.error('❌ Source workflows directory not found:', WORKFLOWS_SRC);
        await waitForKey();
        return;
    }

    if (!ensureDirectoryExists(destination)) {
        await waitForKey();
        return;
    }

    try {
        const files = fs.readdirSync(WORKFLOWS_SRC);
        let count = 0;

        for (const file of files) {
            if (path.extname(file) === '.md') {
                const srcFile = path.join(WORKFLOWS_SRC, file);
                const destFile = path.join(destination, file);
                fs.copyFileSync(srcFile, destFile);
                count++;
            }
        }

        console.log(`✅ Successfully copied ${count} workflows to:`);
        console.log(`   ${destination}`);

    } catch (err) {
        console.error('❌ Failed to copy workflows:', err.message);
    }

    await waitForKey();
}

function waitForKey() {
    return new Promise(resolve => {
        console.log('\nPress any key to continue...');
        const onKey = () => {
            process.stdin.removeListener('keypress', onKey);
            resolve();
        };
        process.stdin.on('keypress', onKey);
    });
}

// --- Render Logic ---

function renderMenu() {
    console.clear();
    console.log(HEADER);
    console.log('Use Arrow Keys to Navigate, ENTER to Select.\n');

    OPTIONS.forEach((opt, index) => {
        const isSelected = index === selectedIndex;
        const pointer = isSelected ? '👉' : '  ';
        const color = isSelected ? '\x1b[36m' : '\x1b[0m'; // Cyan if selected
        const reset = '\x1b[0m';

        console.log(`${pointer} ${color}${opt.label}${reset}`);
        if (isSelected && opt.desc) {
            console.log(`     \x1b[90m${opt.desc}\x1b[0m`); // Gray description
        }
    });
}

// --- Input Handling ---

async function handleSelection() {
    const selectedOption = OPTIONS[selectedIndex];

    // Temporarily disable raw mode if needed or just handle execution
    // Ideally keep raw mode but stop listening to nav keys during execution
    process.stdin.removeListener('keypress', handleInput);

    await selectedOption.action();

    // Resume menu
    renderMenu();
    process.stdin.on('keypress', handleInput);
}

function handleInput(str, key) {
    if (key.name === 'c' && key.ctrl) {
        process.exit();
    }

    if (key.name === 'up') {
        selectedIndex = (selectedIndex - 1 + OPTIONS.length) % OPTIONS.length;
        renderMenu();
    } else if (key.name === 'down') {
        selectedIndex = (selectedIndex + 1) % OPTIONS.length;
        renderMenu();
    } else if (key.name === 'return') {
        handleSelection();
    }
}

// Init
process.stdin.on('keypress', handleInput);
renderMenu();
