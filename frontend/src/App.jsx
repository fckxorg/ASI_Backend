import ReactDOM from 'react-dom';
import React, {Component} from 'react';

import {Router, Route, IndexRoute, browserHistory} from "react-router";

import Layout from "./layouts/Layout.jsx";
import Posts from "./pages/Posts.jsx";
import Post from "./pages/Post.jsx";
import User from "./pages/User.jsx";
import AddPitch from "./pages/AddPitch.jsx";
import Auth from "./pages/Auth.jsx";


ReactDOM.render(
    <Router history={browserHistory}>
        <Route path='/' component={Layout}>
            <IndexRoute component={Posts}/>
            <Route path="auth" component={Auth}/>
            <Route path='user' component={User}/>
            <Route path='create' component={AddPitch}/>
            <Route path='posts' component={Posts}>
                <Route path=':postId' component={Post}/>
            </Route>
        </Route>
    </Router>
, document.getElementById('main'));
