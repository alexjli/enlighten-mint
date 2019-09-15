var current = new XMLHttpRequest();
let query;
current.open('GET', '/current_word', false);
current.onreadystatechange = function() {
  query = current.responseText;
}
current.send();



var client = new XMLHttpRequest();
let response;
client.open('GET', '/' + query + '.json', false);
client.onreadystatechange = function() {
  response = client.responseText;
}
client.send();
definitions = JSON.parse(response);


console.log(query);
console.log(client)

if (typeof definitions === 'string'){
  definitions = [definitions]
}


class VocabTerm extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement("h1", { className: "vocabTerm" }, query)));


  }}


class Definition extends React.Component {
  render() {
    const elements = this.props.categories;
    return (
      React.createElement("div", null,
      elements.map((item, index) =>
      React.createElement("div", { className: "definition" },
      React.createElement("p", { key: index }, item)))));




  }}


class Box extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement(VocabTerm, null),
      React.createElement(Definition, { categories: definitions })));

  }}




// ========================================

ReactDOM.render(
React.createElement(Box, null),
document.getElementById('root'));
