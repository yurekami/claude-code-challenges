export interface Challenge {
  id: string;
  name: string;
  slug: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  timeMinutes: number;
  description: string;
  relatedTips: number[];
}

export interface Category {
  id: string;
  name: string;
  slug: string;
  description: string;
  challenges: Challenge[];
}

export const categories: Category[] = [
  {
    id: 'cli',
    name: 'CLI Fundamentals',
    slug: 'cli-fundamentals',
    description: 'Master the basics of Claude Code',
    challenges: [
      {
        id: 'cli-1',
        name: 'Status Line Setup',
        slug: 'status-line-setup',
        difficulty: 'Easy',
        timeMinutes: 10,
        description: 'Configure your command center',
        relatedTips: [0],
      },
      {
        id: 'cli-2',
        name: 'Slash Commands',
        slug: 'slash-commands',
        difficulty: 'Easy',
        timeMinutes: 12,
        description: 'Learn the shortcuts that matter',
        relatedTips: [1],
      },
      {
        id: 'cli-3',
        name: 'Git Integration',
        slug: 'git-integration',
        difficulty: 'Easy',
        timeMinutes: 15,
        description: 'Seamless version control workflow',
        relatedTips: [4],
      },
      {
        id: 'cli-4',
        name: 'Terminal Aliases',
        slug: 'terminal-aliases',
        difficulty: 'Easy',
        timeMinutes: 10,
        description: 'Speed up your daily commands',
        relatedTips: [7],
      },
      {
        id: 'cli-5',
        name: 'Output Extraction',
        slug: 'output-extraction',
        difficulty: 'Easy',
        timeMinutes: 12,
        description: 'Get data out efficiently',
        relatedTips: [6],
      },
      {
        id: 'cli-6',
        name: 'Fresh Starts',
        slug: 'fresh-starts',
        difficulty: 'Easy',
        timeMinutes: 8,
        description: 'Know when to begin anew',
        relatedTips: [5],
      },
    ],
  },
  {
    id: 'ctx',
    name: 'Context Management',
    slug: 'context-management',
    description: 'Optimize your 200k token window',
    challenges: [
      {
        id: 'ctx-1',
        name: 'Context Compaction',
        slug: 'context-compaction',
        difficulty: 'Medium',
        timeMinutes: 15,
        description: 'Compress without losing meaning',
        relatedTips: [8],
      },
      {
        id: 'ctx-2',
        name: 'Handoff Documents',
        slug: 'handoff-documents',
        difficulty: 'Medium',
        timeMinutes: 18,
        description: 'Perfect session continuity',
        relatedTips: [8],
      },
      {
        id: 'ctx-3',
        name: 'Session Recovery',
        slug: 'session-recovery',
        difficulty: 'Medium',
        timeMinutes: 12,
        description: 'Find and resume any conversation',
        relatedTips: [13],
      },
      {
        id: 'ctx-4',
        name: 'Fork Strategies',
        slug: 'fork-strategies',
        difficulty: 'Medium',
        timeMinutes: 15,
        description: 'Branch your conversations',
        relatedTips: [23],
      },
    ],
  },
  {
    id: 'mcp',
    name: 'MCP Integrations',
    slug: 'mcp-integrations',
    description: 'Extend with external tools',
    challenges: [
      {
        id: 'mcp-1',
        name: 'MCP Server Setup',
        slug: 'mcp-server-setup',
        difficulty: 'Medium',
        timeMinutes: 20,
        description: 'Connect your first MCP server',
        relatedTips: [11, 25],
      },
      {
        id: 'mcp-2',
        name: 'Custom CLAUDE.md',
        slug: 'custom-claude-md',
        difficulty: 'Medium',
        timeMinutes: 15,
        description: 'Craft your default prompt',
        relatedTips: [12],
      },
      {
        id: 'mcp-3',
        name: 'Skill Creation',
        slug: 'skill-creation',
        difficulty: 'Hard',
        timeMinutes: 25,
        description: 'Build reusable capabilities',
        relatedTips: [25],
      },
      {
        id: 'mcp-4',
        name: 'Multi-Tool Workflows',
        slug: 'multi-tool-workflows',
        difficulty: 'Hard',
        timeMinutes: 30,
        description: 'Orchestrate multiple servers',
        relatedTips: [11, 20],
      },
    ],
  },
  {
    id: 'test',
    name: 'Testing & Verification',
    slug: 'testing-verification',
    description: 'Ensure quality and correctness',
    challenges: [
      {
        id: 'test-1',
        name: 'tmux Test Pattern',
        slug: 'tmux-test-pattern',
        difficulty: 'Medium',
        timeMinutes: 20,
        description: 'Autonomous test execution',
        relatedTips: [9],
      },
      {
        id: 'test-2',
        name: 'Git Bisect Debug',
        slug: 'git-bisect-debug',
        difficulty: 'Medium',
        timeMinutes: 18,
        description: 'Find the breaking commit',
        relatedTips: [28],
      },
      {
        id: 'test-3',
        name: 'TDD Workflow',
        slug: 'tdd-workflow',
        difficulty: 'Medium',
        timeMinutes: 25,
        description: 'Test-first development',
        relatedTips: [34],
      },
      {
        id: 'test-4',
        name: 'Output Verification',
        slug: 'output-verification',
        difficulty: 'Medium',
        timeMinutes: 15,
        description: 'Systematic result checking',
        relatedTips: [28],
      },
    ],
  },
  {
    id: 'auto',
    name: 'Workflow Automation',
    slug: 'workflow-automation',
    description: 'Multiply your productivity',
    challenges: [
      {
        id: 'auto-1',
        name: 'Terminal Cascade',
        slug: 'terminal-cascade',
        difficulty: 'Medium',
        timeMinutes: 15,
        description: 'Organize parallel sessions',
        relatedTips: [14],
      },
      {
        id: 'auto-2',
        name: 'Git Worktrees',
        slug: 'git-worktrees',
        difficulty: 'Medium',
        timeMinutes: 20,
        description: 'Work on multiple branches',
        relatedTips: [16],
      },
      {
        id: 'auto-3',
        name: 'CI/CD Integration',
        slug: 'cicd-integration',
        difficulty: 'Hard',
        timeMinutes: 25,
        description: 'Debug GitHub Actions',
        relatedTips: [29],
      },
      {
        id: 'auto-4',
        name: 'Progressive Automation',
        slug: 'progressive-automation',
        difficulty: 'Hard',
        timeMinutes: 30,
        description: 'Automate the automation',
        relatedTips: [41],
      },
    ],
  },
  {
    id: 'adv',
    name: 'Advanced Orchestration',
    slug: 'advanced-orchestration',
    description: 'Master complex workflows',
    challenges: [
      {
        id: 'adv-1',
        name: 'Container Sandbox',
        slug: 'container-sandbox',
        difficulty: 'Hard',
        timeMinutes: 30,
        description: 'Safe execution environments',
        relatedTips: [21],
      },
      {
        id: 'adv-2',
        name: 'Subagent Army',
        slug: 'subagent-army',
        difficulty: 'Hard',
        timeMinutes: 35,
        description: 'Coordinate multiple agents',
        relatedTips: [36],
      },
      {
        id: 'adv-3',
        name: 'Multi-Model Orchestra',
        slug: 'multi-model-orchestra',
        difficulty: 'Hard',
        timeMinutes: 40,
        description: 'Orchestrate different AIs',
        relatedTips: [31],
      },
      {
        id: 'adv-4',
        name: 'Background Execution',
        slug: 'background-execution',
        difficulty: 'Hard',
        timeMinutes: 25,
        description: 'Long-running processes',
        relatedTips: [36],
      },
    ],
  },
];

export const getTotalChallenges = () =>
  categories.reduce((sum, cat) => sum + cat.challenges.length, 0);

export const getCategoryBySlug = (slug: string) =>
  categories.find(cat => cat.slug === slug);

export const getChallengeBySlug = (categorySlug: string, challengeSlug: string) => {
  const category = getCategoryBySlug(categorySlug);
  return category?.challenges.find(ch => ch.slug === challengeSlug);
};
