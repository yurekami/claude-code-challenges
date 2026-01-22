import { test, expect } from '@playwright/test';

test.describe('Claude Code Challenges Terminal', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should display welcome screen on load', async ({ page }) => {
    // Check for welcome ASCII art
    await expect(page.locator('.ascii-art')).toBeVisible();

    // Check for help hint
    await expect(page.getByText("Type 'help' for commands")).toBeVisible();
  });

  test('should show help when typing help command', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('help');
    await input.press('Enter');

    // Check help text appears
    await expect(page.getByText('Available commands:')).toBeVisible();
    await expect(page.getByText('ls')).toBeVisible();
  });

  test('should list categories with ls command', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('ls');
    await input.press('Enter');

    // Check categories appear
    await expect(page.getByText('CLI Fundamentals')).toBeVisible();
    await expect(page.getByText('Context Management')).toBeVisible();
    await expect(page.getByText('MCP Integrations')).toBeVisible();
  });

  test('should navigate to category with cd command', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Navigate to CLI Fundamentals
    await input.fill('cd cli-fundamentals');
    await input.press('Enter');

    // Check prompt changes
    await expect(page.getByText('~/challenges/cli-fundamentals')).toBeVisible();
  });

  test('should show challenges in category with ls after cd', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Navigate to CLI Fundamentals
    await input.fill('cd cli-fundamentals');
    await input.press('Enter');

    // List challenges
    await input.fill('ls');
    await input.press('Enter');

    // Check challenges appear
    await expect(page.getByText('Status Line Setup')).toBeVisible();
    await expect(page.getByText('Slash Commands')).toBeVisible();
  });

  test('should clear terminal with clear command', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Add some output first
    await input.fill('help');
    await input.press('Enter');
    await expect(page.getByText('Available commands:')).toBeVisible();

    // Clear terminal
    await input.fill('clear');
    await input.press('Enter');

    // Welcome should reappear
    await expect(page.locator('.ascii-art')).toBeVisible();
  });

  test('should go back with escape key', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Navigate into category
    await input.fill('cd cli-fundamentals');
    await input.press('Enter');
    await expect(page.getByText('~/challenges/cli-fundamentals')).toBeVisible();

    // Press escape to go back
    await input.press('Escape');

    // Should return to home prompt
    await expect(page.getByText('Returned to home')).toBeVisible();
  });

  test('should autocomplete with tab key', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Type partial command
    await input.fill('he');
    await input.press('Tab');

    // Should autocomplete to 'help'
    await expect(input).toHaveValue('help');
  });

  test('should navigate command history with arrow keys', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Enter some commands
    await input.fill('help');
    await input.press('Enter');
    await input.fill('ls');
    await input.press('Enter');

    // Press up arrow to get previous command
    await input.press('ArrowUp');
    await expect(input).toHaveValue('ls');

    // Press up again for older command
    await input.press('ArrowUp');
    await expect(input).toHaveValue('help');
  });

  test('should show progress statistics', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('progress');
    await input.press('Enter');

    // Check progress display
    await expect(page.getByText('Overall Progress')).toBeVisible();
  });

  test('should start quiz with quiz command', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('quiz');
    await input.press('Enter');

    // Check quiz starts
    await expect(page.getByText('Question 1/3')).toBeVisible();
  });

  test('should show about info', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('about');
    await input.press('Enter');

    // Check about text appears
    await expect(page.getByText('Claude Code Challenges')).toBeVisible();
    await expect(page.getByText('Categories: 6')).toBeVisible();
  });

  test('should handle invalid commands gracefully', async ({ page }) => {
    const input = page.locator('input[type="text"]');
    await input.fill('invalidcommand');
    await input.press('Enter');

    // Should show error message
    await expect(page.getByText("Unknown command: 'invalidcommand'")).toBeVisible();
  });

  test('should support numeric navigation', async ({ page }) => {
    const input = page.locator('input[type="text"]');

    // Navigate with number
    await input.fill('cd 1');
    await input.press('Enter');

    // Should navigate to first category (CLI Fundamentals)
    await expect(page.getByText('~/challenges/cli-fundamentals')).toBeVisible();
  });
});
