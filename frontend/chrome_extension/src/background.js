import { attachHeadersListener } from 'chrome-sidebar'
import { hosts, iframeHosts, url } from './settings'
import React from 'react'
import ReactDOM from 'react-dom'
import { Frame } from 'chrome-sidebar'
import { FrameMint } from './entry'


console.log('Sidebar Extension Registered')

chrome.browserAction.onClicked.addListener(tab => {
  console.log('Browser Action Triggered')
	// for the current tab, inject the "inject.js" file & execute it
	chrome.tabs.executeScript(tab.id, {
    file: 'entry.js'
	})
})

attachHeadersListener({
  webRequest: chrome.webRequest,
  hosts,
  iframeHosts,
  overrideFrameOptions: true
})

chrome.contextMenus.create({
    title: "Enlighten \"%s\"",
    contexts:["selection"],
    onclick: function(info, tab) {
        sendSearch(info.selectionText, tab);
    }
});

chrome.tabs.onUpdated.addListener(
  tab => {
  	// for the current tab, inject the "inject.js" file & execute it
  	chrome.tabs.executeScript(tab.id, {
      file: 'entry.js'
  	})
    chrome.tabs.executeScript(tab.id, {
      file: 'entry.js'
  	})
})

function sendSearch(selectedText, tab){
  console.log('Context Menu Triggered')
  chrome.tabs.sendMessage(tab.id, {vocab: selectedText}, function(response) {
    console.log(response);
  });
  chrome.tabs.executeScript(tab.id, {
    file: 'entry.js'
  })
}
