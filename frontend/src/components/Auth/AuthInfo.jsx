import React, {Component} from 'react';
import {Link} from "react-router";

export default class Auth extends Component {
    constructor(props) {
        super(props);
        this.state = {
            login: '',
            pass: '',
        };
    }

    handleSend = (e) => {
        e.preventDefault();
        // const data = {
        //     login: this.state.login,
        //     password: this.state.pass,
        // };
        // fetch('/user/login/', {
        //     withCredentials: true,
        //     mode: 'cors',
        //     method: 'post',
        //     credentials: 'same-origin',
        //     body: JSON.stringify(data),
        // })
        //     .then(response => response.json())
        //     .then(data => console.log(data.status))
        //     .catch(error => console.log(error));
        this.props.auth();
    };
    handleInputChange = (e) => {
        const prop = e.target.name;
        const val = e.target.value;
        prop === 'login' ? this.setState({login: val}) : this.setState({pass: val,});
    };

    render() {
        return (
            <form method="post">
                <div className="add add-log">
                    <div className="add-post">
                        <p className="add-post-p">Логин</p>
                        <input className="add-post-input" type="text" placeholder="Логин" name="login" onChange={this.handleInputChange}/>
                    </div>
                    <div className="add-post">
                        <p className="add-post-p">Пароль</p>
                        <input className="add-post-input" type="password" placeholder="Пароль" name="pass" onChange={this.handleInputChange}/>
                    </div>
                    <Link to='/'><input className="add-post-btn" value="Войти" onClick={this.handleSend}/></Link>
                </div>
            </form>
        );
    }
}