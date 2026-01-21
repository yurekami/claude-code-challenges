// ASCII art banners for categories
export const categoryArt: Record<string, string> = {
  'cli-fundamentals': `
   ██████╗██╗     ██╗
  ██╔════╝██║     ██║
  ██║     ██║     ██║
  ██║     ██║     ██║
  ╚██████╗███████╗██║
   ╚═════╝╚══════╝╚═╝`,

  'context-management': `
   ██████╗████████╗██╗  ██╗
  ██╔════╝╚══██╔══╝╚██╗██╔╝
  ██║        ██║    ╚███╔╝
  ██║        ██║    ██╔██╗
  ╚██████╗   ██║   ██╔╝ ██╗
   ╚═════╝   ╚═╝   ╚═╝  ╚═╝`,

  'mcp-integrations': `
  ███╗   ███╗ ██████╗██████╗
  ████╗ ████║██╔════╝██╔══██╗
  ██╔████╔██║██║     ██████╔╝
  ██║╚██╔╝██║██║     ██╔═══╝
  ██║ ╚═╝ ██║╚██████╗██║
  ╚═╝     ╚═╝ ╚═════╝╚═╝`,

  'testing-verification': `
  ████████╗███████╗███████╗████████╗
  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
     ██║   █████╗  ███████╗   ██║
     ██║   ██╔══╝  ╚════██║   ██║
     ██║   ███████╗███████║   ██║
     ╚═╝   ╚══════╝╚══════╝   ╚═╝`,

  'workflow-automation': `
  ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
  ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝
  ██║███╗██║██║   ██║██╔══██╗██╔═██╗
  ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
   ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝`,

  'advanced-orchestration': `
   █████╗ ██████╗ ██╗   ██╗
  ██╔══██╗██╔══██╗██║   ██║
  ███████║██║  ██║██║   ██║
  ██╔══██║██║  ██║╚██╗ ██╔╝
  ██║  ██║██████╔╝ ╚████╔╝
  ╚═╝  ╚═╝╚═════╝   ╚═══╝`,
};

export const welcomeArt = `
   ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗
  ██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝
  ██║     ██║     ███████║██║   ██║██║  ██║█████╗
  ██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝
  ╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗
   ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝

   ██████╗ ██████╗ ██████╗ ███████╗
  ██╔════╝██╔═══██╗██╔══██╗██╔════╝
  ██║     ██║   ██║██║  ██║█████╗
  ██║     ██║   ██║██║  ██║██╔══╝
  ╚██████╗╚██████╔╝██████╔╝███████╗
   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝

   ██████╗██╗  ██╗ █████╗ ██╗     ██╗     ███████╗███╗   ██╗ ██████╗ ███████╗███████╗
  ██╔════╝██║  ██║██╔══██╗██║     ██║     ██╔════╝████╗  ██║██╔════╝ ██╔════╝██╔════╝
  ██║     ███████║███████║██║     ██║     █████╗  ██╔██╗ ██║██║  ███╗█████╗  ███████╗
  ██║     ██╔══██║██╔══██║██║     ██║     ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ╚════██║
  ╚██████╗██║  ██║██║  ██║███████╗███████╗███████╗██║ ╚████║╚██████╔╝███████╗███████║
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝`;

export const helpText = `
Available commands:

  help              Show this help message
  ls                List all categories
  ls <category>     List challenges in a category
  cd <category>     Navigate to a category
  start <n>         Start challenge number n
  clear             Clear the terminal
  progress          Show your progress
  about             About Claude Code Challenges

Navigation tips:
  - Click on any [bracketed] item to select it
  - Use Tab to autocomplete commands
  - Press Escape to go back
`;

export const aboutText = `
Claude Code Challenges
======================

Interactive challenges to master Claude Code -
Anthropic's official CLI for Claude.

Based on tips from ykdojo/claude-code-tips

Categories: 6
Challenges: 26
Difficulty: Easy → Hard

Learn by doing. Type 'ls' to get started.
`;

export const getDifficultyBadge = (difficulty: string): string => {
  switch (difficulty) {
    case 'Easy':
      return '[■□□]';
    case 'Medium':
      return '[■■□]';
    case 'Hard':
      return '[■■■]';
    default:
      return '[□□□]';
  }
};

export const getProgressBar = (completed: number, total: number, width: number = 20): string => {
  const filled = Math.round((completed / total) * width);
  const empty = width - filled;
  return '█'.repeat(filled) + '░'.repeat(empty);
};
