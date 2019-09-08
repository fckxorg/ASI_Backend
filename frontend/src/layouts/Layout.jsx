import React, {Component} from 'react';

import './style.css'
import Header from "../components/Header/Header.jsx";
import Auth from "../pages/Auth";

class Layout extends Component {
    constructor(props) {
        super(props);
        this.state = {
            auth: false,
        }
    }
    handleAuth = () => {
        this.setState({
            auth: true,
        });
    };
    render() {
        console.log(this.state.auth);
        if (this.state.auth) {
            return (
                <>
                    <Header/>
                    <div>
                        {this.props.children}
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <Auth auth={this.handleAuth}/>
                </>
            )
        }
    }
}

export default Layout;
