import "./NewChatButton.css";

function NewChatButton({ onClick }) {
  return (
    <button
      className="new-chat-btn"
      onClick={onClick}
    >
      + New Chat
    </button>
  );
}

export default NewChatButton;