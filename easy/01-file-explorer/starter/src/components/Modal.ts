// Modal component

export interface ModalProps {
  title: string;
  content: string;
  isOpen: boolean;
  onClose: () => void;
}

export class Modal {
  private props: ModalProps;

  constructor(props: ModalProps) {
    this.props = props;
  }

  render(): string {
    if (!this.props.isOpen) return '';

    return `
      <div class="modal-overlay">
        <div class="modal">
          <h2>${this.props.title}</h2>
          <div class="modal-content">${this.props.content}</div>
          <button class="close-btn">Close</button>
        </div>
      </div>
    `;
  }

  close(): void {
    this.props.onClose();
  }
}
