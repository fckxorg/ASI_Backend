import React, {Component} from 'react';
import {Link} from "react-router";

class MenuItems extends Component {//рисуются элементы меню
    render() {
        return (
            <li>
                <Link to={this.props.href}>
                    {this.props.children}
                </Link>
            </li>
        );
    }
}

export default MenuItems;
