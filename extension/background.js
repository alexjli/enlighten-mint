class VocabTerm extends React.Component {
    render() {
      return (
        <div>
          <h1 className="vocabTerm">INSERT TERM HERE</h1>
          </div>
      );
    }
  }
  
  class Box extends React.Component {
    render() {
      return (
        <div>
          <VocabTerm />
          <h1 className="box">
            <Definition />
            </h1>
          </div>
      );
    }
  }
  
  class Definition extends React.Component {
    render() {
      return (
        <div className="definition">
          <p>The definition is supposed to be written here.</p>
          </div>
      );
    }
  }
  
  // ========================================
  
  ReactDOM.render(
    <Box />,
    document.getElementById('root')
  );
  