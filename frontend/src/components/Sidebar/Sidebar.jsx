import "./Sidebar.css";
import NewChatButton from "../NewChatButton/NewChatButton";
import ChatItem from "../ChatItem/ChatItem";

function Sidebar({ chats, currentChat, onNewChat, onSelectChat }) {
  return (
    <div className="sidebar">

      <h2>SECE RAG</h2>

      <NewChatButton onClick={onNewChat} />

      <div className="chat-history">

        {chats.length === 0 ? (
          <p className="empty-history">
            No chats yet
          </p>
        ) : (
          chats.map((chat) => (
            <ChatItem
              key={chat.id}
              chat={chat}
              active={chat.id === currentChat}
              onClick={() => onSelectChat(chat.id)}
            />
          ))
        )}

      </div>

    </div>
  );
}

export default Sidebar;