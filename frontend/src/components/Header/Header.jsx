import React, {Component} from 'react';
import {Link} from "react-router";

class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user: [],
        }
    }
    render() {
        const port = 'http://127.0.0.1:8000';
        return (
            <header>
                <div className="header">
                    <div className="name-project">
                        <Link to='/' className="name-project">
                            <img className="name-project-img" src="https://raw.githubusercontent.com/fckxorg/ASI_Backend/master/static/small_logo.png" alt=""/>
                            <div> STARTHUB </div>
                        </Link>
                    </div>
                    <div className="header-right">
                        <Link to='user' className="user">
                            <img src={this.state.user.avatar} alt=""/>
                                <div className="name-user">
                                    <p>{this.state.user.first_name}</p>
                                </div>
                        </Link>
                        <Link to='create'>
                            <button className="add-project">создать проект</button>
                        </Link>
                        {/*<Link to="auth">Sign in</Link>*/}
                    </div>
                    <div>
                        {this.props.children}
                    </div>
                </div>
            </header>
        );
    }
    componentDidMount() {
        fetch('http://127.0.0.1:8000/user/get/')
            .then(response => response.json())
            .then(data => this.setState({user:data}))
    }
}

export default Header;
