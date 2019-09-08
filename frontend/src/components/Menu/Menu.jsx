import React, {Component} from 'react';

class Menu extends Component {// Рисуется меню с элементами из MenuItems
    render() {
        return (
            <nav>
                <ul>
                    {this.props.children}
                </ul>
            </nav>
        );
    }
}

export default Menu;
