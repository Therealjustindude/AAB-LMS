import React from "react";
import {withRouter, Route, Switch} from "react-router-dom";

import SingleCourse from "./Components/SingleCourse";
import Courses from "./Components/Courses";
import User from "./Components/User";
import UserCourses from "./Components/UserCourses";

function Routes() {
  return (
    <Switch>
      <Route exact path="/" component={Courses}/>
      <Route exact path="/Courses/:id" render={(routerProps) => <SingleCourse history={routerProps.history} />}/>
      <Route exact path="/user/:id" render={(routerProps) => <User history={routerProps.history} />}/>
      <Route exact path="/user/:id/courses" render={(routerProps) => <UserCourses history={routerProps.history} />}/>
    </Switch>
  )
}

export default withRouter(Routes)