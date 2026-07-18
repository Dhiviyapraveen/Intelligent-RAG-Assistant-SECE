import "./ChatItem.css";

function ChatItem({
  chat,
  active,
  onClick,
}) {
  return (
    <div
      className={`chat-item ${
        active ? "active-chat" : ""
      }`}
      onClick={onClick}
    >
      💬 {chat.title}
    </div>
  );
}

export default ChatItem;