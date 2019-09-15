var current = new XMLHttpRequest();
let query;
current.open('GET', 'current_word');
current.onreadystatechange = function() {
  query = current.responseText;
}
current.send();

var client = new XMLHttpRequest();
let response;
client.open('GET', query + '.json');
client.onreadystatechange = function() {
  response = client.responseText;
}
client.send();

definitions = JSON.parse(response);

class VocabTerm extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement("h1", { className: "vocabTerm" }, query)));


  }}


class Definition extends React.Component {
  render() {
    return (
      React.createElement("div", { className: "definition" },
      React.createElement("p", null, definitions)));


  }}


class Box extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement(VocabTerm, null),
      React.createElement("h1", { className: "box" },
      React.createElement(Definition, null))));



  }}




// ========================================

ReactDOM.render(
React.createElement(Box, null),
document.getElementById('root'));


class VocabTerm extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement("h1", { className: "vocabTerm" }, "INSERT TERM HERE")));


  }}


class Definition extends React.Component {
  render() {
    return (
      React.createElement("div", { className: "definition" },
      React.createElement("p", null, "The definition is supposed to be written here.")));


  }}


class Box extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement(VocabTerm, null),
      React.createElement("h1", { className: "box" },
      React.createElement(Definition, null))));



  }}




// ========================================

ReactDOM.render(
React.createElement(Box, null),
document.getElementById('root'));
