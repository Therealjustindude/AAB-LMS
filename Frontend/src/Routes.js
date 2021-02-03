import React from "react";
import {withRouter, Route, Switch} from "react-router-dom";

import Home from "./Components/Home";
import Courses from "./Components/Courses";
import Profile from "./Components/Profile";

function Routes() {
  return (
    <Switch>
      <Route path="/Courses" component={Courses}/>
      <Route path="/Profile" component={Profile}/>
      <Route path="/" component={Home}/>
    </Switch>
  )
}

export default withRouter(Routes)