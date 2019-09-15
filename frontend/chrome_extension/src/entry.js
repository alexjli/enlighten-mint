import React from 'react'
import ReactDOM from 'react-dom'
import { Frame } from 'chrome-sidebar'
import { url } from './settings'

export class FrameMint extends Frame {
  constructor(props){
    super(props);
    this.search_term = this.props.search_term;
    this.url = this.props.url;
  }
  static setSearchTerm(term){
    this.search_term = term;
    this.props.url = this.url + this.search_term;
    this.render()
  }
}

if(!Frame.isReady()){
  chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      console.log(sender.tab ?
                  "from a content script:" + sender.tab.url :
                  "from the extension");
      console.log(request.vocab);
      const vocab = request.vocab;
      setURL(vocab);
      sendResponse({farewell: "goodbye"});
  });
}

if (Frame.isReady()) {
  Frame.toggle();
} else {
  boot()
}

function boot() {

  const root = document.createElement('div')
  document.body.appendChild(root)

  const App = (
    <Frame url={url}/>
  )
  console.log(url)

  const frame = ReactDOM.render(App, root)
  const iframe = frame.frame
  iframe.id = "enlightenmint_iframe"
}

function setURL(vocab){
  const iframe = document.getElementById("enlightenmint_iframe");
  iframe.src = url + "?" + vocab;
}

export default FrameMint
