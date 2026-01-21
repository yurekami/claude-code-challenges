/**
 * CLAUDE CODE CHALLENGES - ARCADE CABINET UI
 * Interactive JavaScript for retro gaming experience
 */

// ============================================
// STATE MANAGEMENT
// ============================================
const GameState = {
  score: 0,
  lives: 3,
  currentDifficulty: 'easy',
  soundEnabled: true,
  completedChallenges: new Set(),
  selectedIndex: 0,

  // Load from localStorage
  load() {
    const saved = localStorage.getItem('claudeCodeChallenges');
    if (saved) {
      const data = JSON.parse(saved);
      this.score = data.score || 0;
      this.lives = data.lives || 3;
      this.completedChallenges = new Set(data.completedChallenges || []);
      this.soundEnabled = data.soundEnabled !== false;
    }
    this.updateUI();
  },

  // Save to localStorage
  save() {
    localStorage.setItem('claudeCodeChallenges', JSON.stringify({
      score: this.score,
      lives: this.lives,
      completedChallenges: [...this.completedChallenges],
      soundEnabled: this.soundEnabled
    }));
  },

  // Add points with animation
  addScore(points) {
    const startScore = this.score;
    this.score += points;

    // Animate score counter
    animateScore(startScore, this.score);
    this.save();
  },

  // Mark challenge complete
  completeChallenge(challengeId) {
    if (!this.completedChallenges.has(challengeId)) {
      this.completedChallenges.add(challengeId);
      this.save();
      return true;
    }
    return false;
  },

  // Update all UI elements
  updateUI() {
    document.getElementById('totalScore').textContent =
      this.score.toString().padStart(8, '0');

    document.getElementById('lives').innerHTML =
      '&#9829;'.repeat(this.lives) + '&#9825;'.repeat(3 - this.lives);

    document.getElementById('soundToggle').innerHTML =
      this.soundEnabled ? '&#128266; SOUND: ON' : '&#128264; SOUND: OFF';

    // Update completed cartridges
    this.completedChallenges.forEach(id => {
      const cartridge = document.querySelector(`[data-challenge="${id}"]`);
      if (cartridge) {
        cartridge.classList.add('completed');
        cartridge.classList.remove('locked');
        const status = cartridge.querySelector('.status');
        if (status) {
          status.textContent = 'CLEAR!';
          status.className = 'status status-clear';
        }
      }
    });
  }
};

// ============================================
// SOUND EFFECTS (Web Audio API)
// ============================================
const SoundFX = {
  audioContext: null,

  init() {
    this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
  },

  play(type) {
    if (!GameState.soundEnabled || !this.audioContext) return;

    const oscillator = this.audioContext.createOscillator();
    const gainNode = this.audioContext.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(this.audioContext.destination);

    switch (type) {
      case 'select':
        oscillator.frequency.setValueAtTime(800, this.audioContext.currentTime);
        oscillator.frequency.setValueAtTime(1000, this.audioContext.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.2);
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + 0.2);
        break;

      case 'move':
        oscillator.frequency.setValueAtTime(400, this.audioContext.currentTime);
        gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.05);
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + 0.05);
        break;

      case 'locked':
        oscillator.frequency.setValueAtTime(200, this.audioContext.currentTime);
        oscillator.frequency.setValueAtTime(150, this.audioContext.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.3);
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + 0.3);
        break;

      case 'complete':
        // Victory jingle
        const notes = [523, 659, 784, 1047]; // C, E, G, C
        notes.forEach((freq, i) => {
          const osc = this.audioContext.createOscillator();
          const gain = this.audioContext.createGain();
          osc.connect(gain);
          gain.connect(this.audioContext.destination);
          osc.frequency.setValueAtTime(freq, this.audioContext.currentTime + i * 0.15);
          gain.gain.setValueAtTime(0.2, this.audioContext.currentTime + i * 0.15);
          gain.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + i * 0.15 + 0.3);
          osc.start(this.audioContext.currentTime + i * 0.15);
          osc.stop(this.audioContext.currentTime + i * 0.15 + 0.3);
        });
        return;
    }
  }
};

// ============================================
// ANIMATIONS
// ============================================
function animateScore(from, to) {
  const scoreEl = document.getElementById('totalScore');
  const duration = 500;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    const currentValue = Math.floor(from + (to - from) * easeOutQuart(progress));
    scoreEl.textContent = currentValue.toString().padStart(8, '0');

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

function easeOutQuart(x) {
  return 1 - Math.pow(1 - x, 4);
}

// Pixel Explosion Effect
function createPixelExplosion(x, y, color = '#FEE440') {
  const container = document.getElementById('pixelExplosion');
  const pixelCount = 20;

  for (let i = 0; i < pixelCount; i++) {
    const pixel = document.createElement('div');
    pixel.className = 'pixel';
    pixel.style.left = x + 'px';
    pixel.style.top = y + 'px';
    pixel.style.background = color;

    const angle = (Math.PI * 2 * i) / pixelCount;
    const distance = 50 + Math.random() * 100;
    const tx = Math.cos(angle) * distance;
    const ty = Math.sin(angle) * distance;

    pixel.style.setProperty('--tx', tx + 'px');
    pixel.style.setProperty('--ty', ty + 'px');

    container.appendChild(pixel);

    setTimeout(() => pixel.remove(), 800);
  }
}

// ============================================
// TAB NAVIGATION
// ============================================
function initTabs() {
  const tabs = document.querySelectorAll('.tab-btn');
  const sections = document.querySelectorAll('.cartridge-section');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const difficulty = tab.dataset.difficulty;

      // Update active tab
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Show corresponding section
      sections.forEach(section => {
        if (section.dataset.difficulty === difficulty) {
          section.classList.remove('hidden');
        } else {
          section.classList.add('hidden');
        }
      });

      GameState.currentDifficulty = difficulty;
      GameState.selectedIndex = 0;
      updateCartridgeSelection();
      SoundFX.play('move');
    });
  });
}

// ============================================
// CARTRIDGE INTERACTION
// ============================================
function initCartridges() {
  const cartridges = document.querySelectorAll('.cartridge');

  cartridges.forEach((cartridge, index) => {
    cartridge.addEventListener('click', (e) => {
      if (cartridge.classList.contains('locked')) {
        SoundFX.play('locked');
        shakeElement(cartridge);
        return;
      }

      SoundFX.play('select');
      const rect = cartridge.getBoundingClientRect();
      createPixelExplosion(rect.left + rect.width / 2, rect.top + rect.height / 2);

      // Navigate to challenge
      const challengeId = cartridge.dataset.challenge;
      setTimeout(() => {
        navigateToChallenge(challengeId);
      }, 300);
    });

    cartridge.addEventListener('mouseenter', () => {
      if (!cartridge.classList.contains('locked')) {
        SoundFX.play('move');
      }
    });
  });
}

function shakeElement(element) {
  element.style.animation = 'none';
  element.offsetHeight; // Trigger reflow
  element.style.animation = 'shake 0.5s ease';

  setTimeout(() => {
    element.style.animation = '';
  }, 500);
}

// Add shake animation dynamically
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
  }
`;
document.head.appendChild(shakeStyle);

function updateCartridgeSelection() {
  const currentSection = document.querySelector(
    `.cartridge-section[data-difficulty="${GameState.currentDifficulty}"]`
  );
  const cartridges = currentSection.querySelectorAll('.cartridge');

  cartridges.forEach((c, i) => {
    c.classList.toggle('selected', i === GameState.selectedIndex);
  });
}

// ============================================
// KEYBOARD NAVIGATION
// ============================================
function initKeyboardNav() {
  document.addEventListener('keydown', (e) => {
    const currentSection = document.querySelector(
      `.cartridge-section:not(.hidden)`
    );
    const cartridges = currentSection.querySelectorAll('.cartridge');
    const maxIndex = cartridges.length - 1;

    switch (e.key) {
      case 'ArrowLeft':
        e.preventDefault();
        GameState.selectedIndex = Math.max(0, GameState.selectedIndex - 1);
        updateCartridgeSelection();
        SoundFX.play('move');
        break;

      case 'ArrowRight':
        e.preventDefault();
        GameState.selectedIndex = Math.min(maxIndex, GameState.selectedIndex + 1);
        updateCartridgeSelection();
        SoundFX.play('move');
        break;

      case 'ArrowUp':
        e.preventDefault();
        // Move to previous difficulty
        const tabs = [...document.querySelectorAll('.tab-btn')];
        const currentIndex = tabs.findIndex(t => t.classList.contains('active'));
        if (currentIndex > 0) {
          tabs[currentIndex - 1].click();
        }
        break;

      case 'ArrowDown':
        e.preventDefault();
        // Move to next difficulty
        const tabsDown = [...document.querySelectorAll('.tab-btn')];
        const currentIndexDown = tabsDown.findIndex(t => t.classList.contains('active'));
        if (currentIndexDown < tabsDown.length - 1) {
          tabsDown[currentIndexDown + 1].click();
        }
        break;

      case 'Enter':
        e.preventDefault();
        const selectedCartridge = currentSection.querySelector('.cartridge.selected') ||
          cartridges[GameState.selectedIndex];
        if (selectedCartridge) {
          selectedCartridge.click();
        }
        break;

      case 'Escape':
        // Could be used for back navigation
        break;
    }
  });
}

// ============================================
// NAVIGATION
// ============================================
function navigateToChallenge(challengeId) {
  // Determine difficulty from current section
  const difficulty = GameState.currentDifficulty;

  // Build the path to challenge
  const challengePath = `../${difficulty}/${challengeId}/challenge.md`;

  // For now, open in new tab or show modal
  // In production, this would navigate to the challenge detail page
  window.location.href = `challenge.html?id=${challengeId}&difficulty=${difficulty}`;
}

// ============================================
// SOUND TOGGLE
// ============================================
function initSoundToggle() {
  const btn = document.getElementById('soundToggle');
  btn.addEventListener('click', () => {
    GameState.soundEnabled = !GameState.soundEnabled;
    GameState.save();
    GameState.updateUI();

    if (GameState.soundEnabled) {
      SoundFX.play('select');
    }
  });
}

// ============================================
// UNLOCK LOGIC
// ============================================
function checkUnlocks() {
  // Unlock medium if 3+ easy completed
  const easyCompleted = [...GameState.completedChallenges]
    .filter(id => id.startsWith('0') && parseInt(id) <= 5).length;

  if (easyCompleted >= 3) {
    document.querySelectorAll('[data-difficulty="medium"] .cartridge').forEach(c => {
      if (!GameState.completedChallenges.has(c.dataset.challenge)) {
        c.classList.remove('locked');
        c.querySelector('.status').textContent = 'NEW!';
        c.querySelector('.status').className = 'status status-new';
      }
    });
  }

  // Unlock hard if 3+ medium completed
  const mediumCompleted = [...GameState.completedChallenges]
    .filter(id => id.includes('pr') || id.includes('context') ||
      id.includes('parallel') || id.includes('config') || id.includes('refactor')).length;

  if (mediumCompleted >= 3) {
    document.querySelectorAll('[data-difficulty="hard"] .cartridge').forEach(c => {
      if (!GameState.completedChallenges.has(c.dataset.challenge)) {
        c.classList.remove('locked');
        c.querySelector('.status').textContent = 'NEW!';
        c.querySelector('.status').className = 'status status-new';
      }
    });
  }
}

// ============================================
// DEMO: Simulate completing a challenge
// ============================================
function demoComplete(challengeId, points) {
  if (GameState.completeChallenge(challengeId)) {
    GameState.addScore(points);
    SoundFX.play('complete');

    const cartridge = document.querySelector(`[data-challenge="${challengeId}"]`);
    if (cartridge) {
      const rect = cartridge.getBoundingClientRect();
      createPixelExplosion(rect.left + rect.width / 2, rect.top + rect.height / 2, '#39FF14');
    }

    GameState.updateUI();
    checkUnlocks();
  }
}

// Expose for testing
window.demoComplete = demoComplete;

// ============================================
// INITIALIZATION
// ============================================
document.addEventListener('DOMContentLoaded', () => {
  // Initialize audio context on first user interaction
  document.addEventListener('click', () => {
    if (!SoundFX.audioContext) {
      SoundFX.init();
    }
  }, { once: true });

  GameState.load();
  initTabs();
  initCartridges();
  initKeyboardNav();
  initSoundToggle();
  checkUnlocks();
  updateCartridgeSelection();

  console.log('%c CLAUDE CODE CHALLENGES ', 'background: #FF006E; color: #FEE440; font-size: 20px; font-weight: bold;');
  console.log('%c Arcade Mode Activated! ', 'background: #00F5D4; color: #1B0030; font-size: 14px;');
  console.log('Demo: window.demoComplete("01-file-explorer", 100)');
});
