import React, {Component} from 'react';
import AuthInfo from "../components/Auth/AuthInfo";

class Auth extends Component {
    render() {
        return (
            <AuthInfo auth={this.props.auth}/>
        );
    }
}

export default Auth;