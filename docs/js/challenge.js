/**
 * CHALLENGE DETAIL PAGE - JavaScript
 */

// Challenge data mapping
const CHALLENGES = {
  'easy': {
    '01-file-explorer': {
      name: 'FILE EXPLORER',
      icon: '&#128193;',
      points: 100,
      mission: 'Navigate a project directory using Claude Code\'s file exploration tools. Your mission: Find specific files and extract critical information using Glob, Read, and Grep tools.',
      objectives: [
        { text: 'Find all TypeScript files (.ts)', points: 25 },
        { text: 'Locate the calculateTotal function', points: 25 },
        { text: 'Read database.json config', points: 25 },
        { text: 'Count lines in helpers.ts', points: 25 }
      ],
      constraints: [
        { type: 'warning', text: 'Do NOT use bash commands (find, cat, wc)' },
        { type: 'info', text: 'Use only Claude Code tools (Glob, Read, Grep)' },
        { type: 'info', text: 'Complete in a single session' }
      ],
      hints: [
        'Use Glob with pattern "**/*.ts" for recursive TypeScript search',
        'Use Grep with output_mode "content" and -n flag for line numbers'
      ]
    },
    '02-quick-commit': {
      name: 'QUICK COMMIT',
      icon: '&#128190;',
      points: 100,
      mission: 'Create a proper git commit following conventional commit standards. Claude Code excels at analyzing changes and crafting appropriate commit messages.',
      objectives: [
        { text: 'Stage the modified files', points: 25 },
        { text: 'Analyze changes to understand modifications', points: 25 },
        { text: 'Create conventional commit message', points: 25 },
        { text: 'Include Co-Authored-By footer', points: 25 }
      ],
      constraints: [
        { type: 'warning', text: 'Do NOT use --amend flag' },
        { type: 'warning', text: 'Do NOT use placeholder text' },
        { type: 'info', text: 'Follow conventional commit format' }
      ],
      hints: [
        'Use git diff to see what changed',
        'Types: feat, fix, docs, style, refactor, test, chore'
      ]
    },
    '03-token-check': {
      name: 'TOKEN CHECK',
      icon: '&#127918;',
      points: 100,
      mission: 'Understanding token usage is crucial for efficient Claude Code sessions. Monitor and report on your token consumption using built-in commands.',
      objectives: [
        { text: 'Check current usage with /usage', points: 30 },
        { text: 'Report context usage percentage', points: 20 },
        { text: 'Make compaction recommendation', points: 25 },
        { text: 'Explain when to use /compact', points: 25 }
      ],
      constraints: [
        { type: 'info', text: 'Use only Claude Code slash commands' },
        { type: 'info', text: 'Report accurate numbers from YOUR session' }
      ],
      hints: [
        'Run /usage first to see your current stats',
        'Context above 80% suggests compaction'
      ]
    },
    '04-simple-edit': {
      name: 'SIMPLE EDIT',
      icon: '&#9998;',
      points: 100,
      mission: 'Master Claude Code\'s Edit tool for making precise, targeted changes to files. The Edit tool uses exact string matching to replace content.',
      objectives: [
        { text: 'Fix typo: usrName → userName', points: 25 },
        { text: 'Update return type to Promise<Data>', points: 25 },
        { text: 'Add type to processItem parameter', points: 25 },
        { text: 'Update import statement', points: 25 }
      ],
      constraints: [
        { type: 'warning', text: 'Use ONLY the Edit tool (not Write)' },
        { type: 'info', text: 'old_string must match EXACTLY' },
        { type: 'info', text: 'Make minimal, targeted edits' }
      ],
      hints: [
        'Read the file first to see exact content',
        'Include enough context for unique matches'
      ]
    },
    '05-search-master': {
      name: 'SEARCH MASTER',
      icon: '&#128269;',
      points: 100,
      mission: 'Efficient codebase navigation requires mastering Claude Code\'s search tools. Learn to use Grep and Glob to find code patterns quickly.',
      objectives: [
        { text: 'Find all files containing TODO comments', points: 25 },
        { text: 'Find all async function definitions', points: 25 },
        { text: 'Find all imports from @/utils', points: 25 },
        { text: 'Count console.log occurrences', points: 25 }
      ],
      constraints: [
        { type: 'warning', text: 'Do NOT use bash grep, find, or rg' },
        { type: 'info', text: 'Use Grep for content searching' },
        { type: 'info', text: 'Use Glob for file pattern matching' }
      ],
      hints: [
        'Use output_mode: "files_with_matches" for file lists',
        'Use output_mode: "count" for statistics'
      ]
    }
  },
  'medium': {
    '01-pr-creator': { name: 'PR CREATOR', icon: '&#128640;', points: 150 },
    '02-context-handoff': { name: 'CONTEXT HANDOFF', icon: '&#128203;', points: 150 },
    '03-parallel-search': { name: 'PARALLEL SEARCH', icon: '&#9881;', points: 150 },
    '04-config-detective': { name: 'CONFIG DETECTIVE', icon: '&#128270;', points: 150 },
    '05-refactor-safely': { name: 'REFACTOR SAFELY', icon: '&#128295;', points: 150 }
  },
  'hard': {
    '01-full-feature-flow': { name: 'FULL FEATURE FLOW', icon: '&#128293;', points: 250 },
    '02-mcp-orchestra': { name: 'MCP ORCHESTRA', icon: '&#127932;', points: 250 },
    '03-autonomous-debug': { name: 'AUTONOMOUS DEBUG', icon: '&#128375;', points: 250 }
  }
};

// Page state
const ChallengeState = {
  difficulty: 'easy',
  challengeId: '01-file-explorer',
  startTime: null,
  hintsUsed: 0,
  timerInterval: null
};

// Parse URL parameters
function getUrlParams() {
  const params = new URLSearchParams(window.location.search);
  return {
    id: params.get('id') || '01-file-explorer',
    difficulty: params.get('difficulty') || 'easy'
  };
}

// Load challenge data
function loadChallenge() {
  const params = getUrlParams();
  ChallengeState.difficulty = params.difficulty;
  ChallengeState.challengeId = params.id;

  const challenge = CHALLENGES[params.difficulty]?.[params.id];

  if (!challenge) {
    console.error('Challenge not found:', params);
    return;
  }

  // Update header
  document.getElementById('difficultyBadge').textContent = params.difficulty.toUpperCase();
  document.getElementById('difficultyBadge').className = `difficulty-badge ${params.difficulty}`;

  const stageNum = params.id.split('-')[0];
  document.getElementById('stageBadge').textContent = `STAGE ${parseInt(stageNum)}`;

  // Update title section
  document.getElementById('challengeIcon').innerHTML = challenge.icon;
  document.getElementById('challengeName').textContent = challenge.name;
  document.getElementById('pointsValue').textContent = challenge.points;

  // Update mission
  if (challenge.mission) {
    document.getElementById('missionContent').innerHTML = `<p>${challenge.mission}</p>`;
  }

  // Update objectives
  if (challenge.objectives) {
    const objectiveList = document.getElementById('objectiveList');
    objectiveList.innerHTML = challenge.objectives.map(obj => `
      <li class="objective">
        <span class="checkbox">&#9744;</span>
        <span class="objective-text">${obj.text}</span>
        <span class="objective-points">+${obj.points}</span>
      </li>
    `).join('');
  }

  // Update constraints
  if (challenge.constraints) {
    const constraintList = document.getElementById('constraintList');
    constraintList.innerHTML = challenge.constraints.map(c => `
      <li class="constraint ${c.type}">
        <span class="constraint-icon">${c.type === 'warning' ? '&#10060;' : '&#9989;'}</span>
        ${c.text}
      </li>
    `).join('');
  }

  // Update page title
  document.title = `${challenge.name} - Claude Code Challenges`;
}

// Timer functions
function startTimer() {
  ChallengeState.startTime = Date.now();
  ChallengeState.timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
  if (!ChallengeState.startTime) return;

  const elapsed = Date.now() - ChallengeState.startTime;
  const minutes = Math.floor(elapsed / 60000);
  const seconds = Math.floor((elapsed % 60000) / 1000);

  document.getElementById('timer').textContent =
    `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function stopTimer() {
  if (ChallengeState.timerInterval) {
    clearInterval(ChallengeState.timerInterval);
  }
}

// Hint system
function initHints() {
  document.querySelectorAll('.hint-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const hintNum = btn.dataset.hint;
      const hintContent = document.getElementById(`hint${hintNum}`);

      if (hintContent.classList.contains('hidden')) {
        hintContent.classList.remove('hidden');
        btn.querySelector('.hint-status').innerHTML = '&#128275; REVEALED';
        ChallengeState.hintsUsed++;

        if (typeof SoundFX !== 'undefined') {
          SoundFX.play('select');
        }
      }
    });
  });
}

// Button handlers
function initButtons() {
  const startBtn = document.getElementById('startBtn');
  const verifyBtn = document.getElementById('verifyBtn');

  startBtn.addEventListener('click', () => {
    startTimer();
    startBtn.innerHTML = '<span class="btn-icon">&#127918;</span> CHALLENGE STARTED!';
    startBtn.disabled = true;
    startBtn.style.animation = 'none';

    // Add terminal output
    addTerminalLine('Challenge started! Good luck, player!');
    addTerminalLine(`Navigate to: ${ChallengeState.difficulty}/${ChallengeState.challengeId}/`);

    if (typeof SoundFX !== 'undefined') {
      SoundFX.play('select');
    }
  });

  verifyBtn.addEventListener('click', () => {
    addTerminalLine('Running verification...');
    addTerminalLine('$ python tests.py');

    // Simulate verification (in real app, would call actual test runner)
    setTimeout(() => {
      // Demo: Show victory for testing
      showVictory(100, 25, ChallengeState.hintsUsed * 10);
    }, 1500);
  });
}

// Terminal output
function addTerminalLine(text) {
  const terminal = document.getElementById('terminalOutput');
  const blinkLine = terminal.querySelector('.blink');

  const newLine = document.createElement('p');
  newLine.className = 'terminal-line';
  newLine.innerHTML = `<span class="prompt">$</span> ${text}`;

  terminal.insertBefore(newLine, blinkLine);
  terminal.scrollTop = terminal.scrollHeight;
}

// Victory modal
function showVictory(baseScore, timeBonus, hintPenalty) {
  stopTimer();

  const total = baseScore + timeBonus - hintPenalty;

  document.getElementById('baseScore').textContent = `+${baseScore}`;
  document.getElementById('timeBonus').textContent = `+${timeBonus}`;
  document.getElementById('hintPenalty').textContent = `-${hintPenalty}`;
  document.getElementById('totalEarned').textContent = `+${total}`;

  document.getElementById('victoryModal').classList.remove('hidden');

  // Update game state
  if (typeof GameState !== 'undefined') {
    GameState.completeChallenge(ChallengeState.challengeId);
    GameState.addScore(total);
  }

  if (typeof SoundFX !== 'undefined') {
    SoundFX.play('complete');
  }

  // Pixel explosion
  if (typeof createPixelExplosion === 'function') {
    const modal = document.querySelector('.modal-content');
    const rect = modal.getBoundingClientRect();
    createPixelExplosion(rect.left + rect.width / 2, rect.top, '#39FF14');
  }
}

// Keyboard shortcuts
function initKeyboard() {
  document.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'Escape':
        window.location.href = 'index.html';
        break;
      case 'Enter':
        if (!ChallengeState.startTime) {
          document.getElementById('startBtn').click();
        }
        break;
      case 'h':
      case 'H':
        const firstHint = document.querySelector('.hint-btn');
        if (firstHint) firstHint.click();
        break;
    }
  });
}

// Update score display
function updateScoreDisplay() {
  if (typeof GameState !== 'undefined') {
    document.getElementById('currentScore').textContent =
      `SCORE: ${GameState.score.toString().padStart(8, '0')}`;
  }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  loadChallenge();
  initHints();
  initButtons();
  initKeyboard();
  updateScoreDisplay();

  // Initialize audio on interaction
  document.addEventListener('click', () => {
    if (typeof SoundFX !== 'undefined' && !SoundFX.audioContext) {
      SoundFX.init();
    }
  }, { once: true });
});
