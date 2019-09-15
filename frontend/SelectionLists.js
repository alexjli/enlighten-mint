function SelectionItem (props) {
  return(
    <label className="container">
     <input className = "selectionItem" type={props.type} name={props.type} onClick={props.onClick}></input>
     <span className={props.type}></span>
     {props.value}
    </label>
  );
}

class SelectionList extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      categories: this.props.categories,
      type: this.props.type,
      selected: this.props.selected_array,
      selected_callback: this.props.selected_callback,
    };
  }

  handleClick(i){
    if (this.state.type == 'radio') {
      this.state.selected = Array(this.state.selected.length).fill(false);
      this.state.selected[i] = true;
    } else if (this.state.type == 'checkbox') {
      this.state.selected[i] = !this.state.selected[i];
    }
    this.state.selected_callback(this.state.selected);
    console.log(this.state.selected);
  }

  render(){
    const elements = this.props.categories;
    return (
      <div>
        {elements.map((item, index) => (
          <SelectionItem key={index} value={item} type={this.state.type} onClick={() => this.handleClick(index)}/>
        ))}
      </div>
    );
  }
}

class Form extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      categories: this.props.categories,
      selected_array: Array(this.props.categories.length).fill(false),
    };
    this.setSelectedArray = this.setSelectedArray.bind(this)
  }

  setSelectedArray(selected){
    this.state.selected_array = selected;
  }

  submitForm(){
    console.log(this.state.selected_array);
    ReactDOM.unmountComponentAtNode(
      document.getElementById("root")
    )
    ReactDOM.render(
      <Form categories={['A', 'B', 'C']} selected_array={Array(3).fill(false)}/>,
      document.getElementById("root")
    )
  }

  render(){
    return(
      <div>
        <SelectionList
          className="selectionList"
          categories={this.state.categories}
          selected_array={this.state.selected_array}
          type="checkbox"
          selected_callback={this.setSelectedArray}/>
        <button className="submit" onClick={() => this.submitForm()}> Continue </button>
      </div>
    );
  }
}
