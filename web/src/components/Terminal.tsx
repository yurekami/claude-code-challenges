'use client';

import { useState, useRef, useEffect, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { categories, Category, Challenge, getTotalChallenges } from '@/data/challenges';
import {
  welcomeArt,
  categoryArt,
  helpText,
  aboutText,
  getDifficultyBadge,
  getProgressBar,
} from '@/lib/ascii';

interface OutputLine {
  id: string;
  content: React.ReactNode;
  type: 'output' | 'command' | 'error' | 'success' | 'ascii';
}

// Generate unique ID for output lines
const genId = () => Math.random().toString(36).substr(2, 9);

// Initial welcome output
const getInitialOutput = (): OutputLine[] => [
  { id: genId(), content: <pre className="ascii-art text-[#F778BA]">{welcomeArt}</pre>, type: 'ascii' },
  { id: genId(), content: '', type: 'output' },
  { id: genId(), content: <span className="text-[#8B949E]">Type &apos;help&apos; for commands or &apos;ls&apos; to see categories</span>, type: 'output' },
  { id: genId(), content: '', type: 'output' },
];

export default function Terminal() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState<OutputLine[]>(getInitialOutput);
  const [currentCategory, setCurrentCategory] = useState<Category | null>(null);
  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const [completedChallenges] = useState<Set<string>>(new Set());

  const inputRef = useRef<HTMLInputElement>(null);
  const outputRef = useRef<HTMLDivElement>(null);

  // Add output line
  const addOutput = useCallback((content: React.ReactNode, type: OutputLine['type'] = 'output') => {
    setOutput(prev => [...prev, { id: genId(), content, type }]);
  }, []);

  // Start a challenge
  const startChallenge = useCallback((ch: Challenge, catSlug: string | undefined) => {
    addOutput('');
    addOutput(<span className="text-[#3FB950]">Loading challenge...</span>, 'success');
    addOutput(
      <div className="my-2">
        <span className="text-[#3FB950]">{getProgressBar(60, 100)}</span>
        <span className="text-[#8B949E] ml-2">60%</span>
      </div>
    );

    setTimeout(() => {
      addOutput('');
      addOutput(
        <div className="border border-[#30363D] p-4 rounded my-2">
          <div className="text-[#F778BA] font-bold text-lg mb-2">{ch.name}</div>
          <div className="text-[#8B949E] mb-2">
            {ch.difficulty} • {ch.timeMinutes} minutes • Tips: {ch.relatedTips.join(', ')}
          </div>
          <div className="text-[#C9D1D9] mb-4">{ch.description}</div>
          <div className="text-[#58A6FF]">
            Challenge loaded! Open /challenges/{catSlug}/{ch.slug}/ in your editor.
          </div>
        </div>
      );
      addOutput('');
      addOutput(<span className="text-[#8B949E]">When complete, type &apos;complete {ch.id}&apos; to mark as done</span>);
    }, 500);
  }, [addOutput]);

  // List challenges in category
  const listChallenges = useCallback((cat: Category) => {
    cat.challenges.forEach((ch, i) => {
      const isComplete = completedChallenges.has(ch.id);
      const badge = getDifficultyBadge(ch.difficulty);

      addOutput(
        <div className="flex items-start gap-2 my-1">
          <span
            className={`${isComplete ? 'text-[#3FB950]' : 'text-[#58A6FF]'} clickable cursor-pointer`}
            onClick={() => {
              startChallenge(ch, cat.slug);
              inputRef.current?.focus();
            }}
          >
            [{i + 1}]
          </span>
          <div className="flex-1">
            <span
              className={`${isComplete ? 'text-[#3FB950]' : 'text-[#C9D1D9]'} clickable cursor-pointer hover:text-[#58A6FF]`}
              onClick={() => {
                startChallenge(ch, cat.slug);
                inputRef.current?.focus();
              }}
            >
              {ch.name}
            </span>
            <span className={`ml-2 ${ch.difficulty === 'Easy' ? 'text-[#3FB950]' : ch.difficulty === 'Medium' ? 'text-[#D29922]' : 'text-[#F85149]'}`}>
              {badge}
            </span>
            <span className="text-[#8B949E] ml-2">{ch.timeMinutes}m</span>
          </div>
        </div>
      );
      addOutput(<span className="text-[#8B949E] ml-6 text-sm">&quot;{ch.description}&quot;</span>);
    });
    addOutput('');
    addOutput(<span className="text-[#8B949E]">Type &apos;start &lt;n&gt;&apos; or click to begin</span>);
  }, [addOutput, completedChallenges, startChallenge]);

  // Show category with ASCII art
  const showCategory = useCallback((cat: Category) => {
    const art = categoryArt[cat.slug];
    if (art) {
      addOutput(<pre className="ascii-art">{art}</pre>, 'ascii');
    }
    addOutput('');
    addOutput(
      <div>
        <span className="text-[#F778BA] font-bold">{cat.name.toUpperCase()}</span>
        <span className="text-[#8B949E] ml-4">{cat.challenges.length} challenges</span>
      </div>
    );
    addOutput(<span className="text-[#8B949E]">{cat.description}</span>);
    addOutput('');
    listChallenges(cat);
  }, [addOutput, listChallenges]);

  // List categories
  const listCategories = useCallback(() => {
    addOutput(<span className="text-[#8B949E]">Categories ({categories.length}):</span>);
    addOutput('');

    categories.forEach((cat, i) => {
      const completed = cat.challenges.filter(c => completedChallenges.has(c.id)).length;
      const total = cat.challenges.length;

      addOutput(
        <div className="flex items-start gap-4">
          <span
            className="text-[#58A6FF] clickable cursor-pointer hover:underline"
            onClick={() => {
              setCurrentCategory(cat);
              showCategory(cat);
              inputRef.current?.focus();
            }}
          >
            [{i + 1}]
          </span>
          <div className="flex-1">
            <span
              className="text-[#C9D1D9] clickable cursor-pointer hover:text-[#58A6FF]"
              onClick={() => {
                setCurrentCategory(cat);
                showCategory(cat);
                inputRef.current?.focus();
              }}
            >
              {cat.name}
            </span>
            <span className="text-[#8B949E] ml-4">
              {completed}/{total}
            </span>
          </div>
        </div>
      );
    });

    addOutput('');
    addOutput(<span className="text-[#8B949E]">Type &apos;cd &lt;category&gt;&apos; or click to navigate</span>);
  }, [addOutput, completedChallenges, showCategory]);

  // Show progress
  const showProgress = useCallback(() => {
    const total = getTotalChallenges();
    const completed = completedChallenges.size;
    const percent = Math.round((completed / total) * 100);

    addOutput('');
    addOutput(<span className="text-[#F778BA] font-bold">YOUR PROGRESS</span>);
    addOutput('');
    addOutput(
      <div>
        <span className="text-[#3FB950]">{getProgressBar(completed, total, 30)}</span>
        <span className="text-[#C9D1D9] ml-2">{completed}/{total}</span>
        <span className="text-[#8B949E] ml-2">({percent}%)</span>
      </div>
    );
    addOutput('');

    categories.forEach(cat => {
      const catCompleted = cat.challenges.filter(c => completedChallenges.has(c.id)).length;
      const catTotal = cat.challenges.length;

      addOutput(
        <div className="flex items-center gap-2">
          <span className="text-[#C9D1D9] w-32">{cat.name}</span>
          <span className="text-[#3FB950]">{getProgressBar(catCompleted, catTotal, 10)}</span>
          <span className="text-[#8B949E]">{catCompleted}/{catTotal}</span>
        </div>
      );
    });
  }, [addOutput, completedChallenges]);

  // Command processor - now all helper functions are declared above
  const processCommand = useCallback((cmd: string) => {
    const trimmed = cmd.trim().toLowerCase();
    const parts = trimmed.split(/\s+/);
    const command = parts[0];
    const args = parts.slice(1);

    // Add command to output
    addOutput(
      <span>
        <span className="text-[#58A6FF]">$ </span>
        <span>{cmd}</span>
      </span>,
      'command'
    );

    // Process commands
    switch (command) {
      case 'help':
        addOutput(<pre className="text-[#C9D1D9] whitespace-pre-wrap">{helpText}</pre>);
        break;

      case 'about':
        addOutput(<pre className="text-[#C9D1D9] whitespace-pre-wrap">{aboutText}</pre>);
        break;

      case 'clear':
        setOutput([]);
        break;

      case 'ls':
        if (args[0]) {
          const cat = categories.find(c =>
            c.slug === args[0] || c.slug.startsWith(args[0]) || c.id === args[0]
          );
          if (cat) {
            listChallenges(cat);
          } else {
            addOutput(<span className="text-red-400">Category not found: {args[0]}</span>, 'error');
          }
        } else if (currentCategory) {
          listChallenges(currentCategory);
        } else {
          listCategories();
        }
        break;

      case 'cd':
        if (args[0] === '..' || args[0] === '~') {
          setCurrentCategory(null);
          addOutput(<span className="text-[#3FB950]">Returned to home</span>, 'success');
        } else if (args[0]) {
          const cat = categories.find(c =>
            c.slug === args[0] || c.slug.startsWith(args[0]) || c.id === args[0]
          );
          if (cat) {
            setCurrentCategory(cat);
            showCategory(cat);
          } else {
            addOutput(<span className="text-red-400">Category not found: {args[0]}</span>, 'error');
          }
        } else {
          addOutput(<span className="text-[#8B949E]">Usage: cd &lt;category&gt;</span>);
        }
        break;

      case 'start':
        if (args[0] && currentCategory) {
          const num = parseInt(args[0]);
          if (num > 0 && num <= currentCategory.challenges.length) {
            startChallenge(currentCategory.challenges[num - 1], currentCategory.slug);
          } else {
            addOutput(<span className="text-red-400">Invalid challenge number</span>, 'error');
          }
        } else if (!currentCategory) {
          addOutput(<span className="text-[#8B949E]">Navigate to a category first: cd &lt;category&gt;</span>);
        } else {
          addOutput(<span className="text-[#8B949E]">Usage: start &lt;number&gt;</span>);
        }
        break;

      case 'progress':
        showProgress();
        break;

      case '':
        break;

      default:
        addOutput(
          <span className="text-red-400">
            Command not found: {command}. Type &apos;help&apos; for available commands.
          </span>,
          'error'
        );
    }

    // Add to history
    if (trimmed) {
      setCommandHistory(prev => [...prev, trimmed]);
      setHistoryIndex(-1);
    }
  }, [addOutput, currentCategory, listChallenges, listCategories, showCategory, startChallenge, showProgress]);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // Auto-scroll
  useEffect(() => {
    if (outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight;
    }
  }, [output]);

  // Handle input
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      processCommand(input);
      setInput('');
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (commandHistory.length > 0) {
        const newIndex = historyIndex < commandHistory.length - 1 ? historyIndex + 1 : historyIndex;
        setHistoryIndex(newIndex);
        setInput(commandHistory[commandHistory.length - 1 - newIndex] || '');
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setInput(commandHistory[commandHistory.length - 1 - newIndex] || '');
      } else {
        setHistoryIndex(-1);
        setInput('');
      }
    } else if (e.key === 'Tab') {
      e.preventDefault();
      // Simple tab completion
      const commands = ['help', 'ls', 'cd', 'start', 'clear', 'progress', 'about'];
      const catSlugs = categories.map(c => c.slug);
      const all = [...commands, ...catSlugs];
      const match = all.find(c => c.startsWith(input.toLowerCase()));
      if (match) setInput(match);
    } else if (e.key === 'Escape') {
      if (currentCategory) {
        setCurrentCategory(null);
        addOutput(<span className="text-[#3FB950]">Returned to home</span>, 'success');
      }
    }
  };

  // Get prompt
  const getPrompt = () => {
    if (currentCategory) {
      return `~/challenges/${currentCategory.slug}`;
    }
    return '~';
  };

  return (
    <div
      className="terminal min-h-screen flex flex-col"
      onClick={() => inputRef.current?.focus()}
    >
      {/* Output area */}
      <div
        ref={outputRef}
        className="flex-1 overflow-y-auto pb-4"
      >
        <AnimatePresence>
          {output.map((line) => (
            <motion.div
              key={line.id}
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.1 }}
              className="leading-relaxed"
            >
              {line.content}
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {/* Input area */}
      <div className="sticky bottom-0 bg-[#0D1117] border-t border-[#30363D] py-3 flex items-center gap-2">
        <span className="text-[#3FB950]">{getPrompt()}</span>
        <span className="text-[#58A6FF]">$</span>
        <input
          ref={inputRef}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          className="command-input flex-1"
          placeholder="Type a command..."
          autoFocus
          spellCheck={false}
          autoComplete="off"
        />
        <span className="cursor" />
      </div>

      {/* Status bar */}
      <div className="bg-[#161B22] border-t border-[#30363D] px-4 py-1 flex items-center justify-between text-xs text-[#8B949E]">
        <span>Claude Code Challenges</span>
        <span>{completedChallenges.size}/{getTotalChallenges()} completed</span>
        <span>[ESC: back] [TAB: complete]</span>
      </div>
    </div>
  );
}
