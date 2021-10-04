import Layout from "./components/layout";
import { Widget, addResponseMessage, setQuickButtons, toggleMsgLoader, addUserMessage } from 'react-chat-widget';

import 'react-chat-widget/lib/styles.css';


function App() {


  const handleNewUserMessage = (newMessage) => {

    toggleMsgLoader();
    setQuickButtons([])
    fetch("http://127.0.0.1:8080/api/agent/chat", {
      method: "POST",
      headers: {'Content-Type':"application/json"},
      body: JSON.stringify({ message: newMessage })
    }).then(res => res.json()).then(res => {
      addResponseMessage(res.message)
    }).finally(_ => {
      toggleMsgLoader();
    })



    // ChatPostRequest('/agent/chat', { message: newMessage }).then((res) => {
    //   clearTimeout(timeout);
    //   addResponseMessage(res.message)
    //   setQuickButtons(res.options)|
    //   toggleMsgLoader();
    // }).catch((err) => {
    //   clearTimeout(timeout);
    //   toggleMsgLoader();
    // })
  };

  return (
    <Layout>
      <Widget
        handleNewUserMessage={handleNewUserMessage}
        showCloseButton={false}
        profileAvatar="https://i.ibb.co/rGm1SKy/robot.gif"
        titleAvatar="https://i.ibb.co/rGm1SKy/robot.gif"
        fullScreenMode={false}
        subtitle="" />
    </Layout>
  );
}

export default App;
