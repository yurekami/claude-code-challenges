// Button component

export interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'danger';
}

export class Button {
  private props: ButtonProps;

  constructor(props: ButtonProps) {
    this.props = props;
  }

  render(): string {
    const { label, disabled, variant = 'primary' } = this.props;
    return `<button class="${variant}" ${disabled ? 'disabled' : ''}>${label}</button>`;
  }

  click(): void {
    if (!this.props.disabled) {
      this.props.onClick();
    }
  }
}
