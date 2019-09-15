const usr = 'eda'
var client = new XMLHttpRequest();
let words;
client.open('GET', '/users/' + usr + '.json', false);
client.onreadystatechange = function() {
  words = client.responseText;
}
client.send();

wordbank = JSON.parse(words);
console.log(wordbank)

class Vocab extends React.Component {
  constructor(props){
    super(props);
  }
  onClick(){

  }
  render() {
    const elements = this.props.categories;
      return (
        React.createElement("div", null,
        elements.map((item, index) =>
        React.createElement("div", { className: "definition"},
        React.createElement("a", { key: index, href:"/define.html?"+item }, item)))));
  }}


class Box extends React.Component {
  render() {
    return (
      React.createElement("div", null,
      React.createElement(Vocab, { categories: wordbank })));

  }}




// ========================================

ReactDOM.render(
React.createElement(Box, null),
document.getElementById('root'));
