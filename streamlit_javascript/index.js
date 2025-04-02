import React from "react";
import { StreamlitComponentBase, withStreamlitConnection } from "streamlit-component-lib";

class MyComponent extends StreamlitComponentBase {
  render() {
    return <div>Hello from custom JavaScript!</div>;
  }
}

export default withStreamlitConnection(MyComponent);
