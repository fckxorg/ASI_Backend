import React, {Component} from 'react';
import {Link} from "react-router";

class PostMinInfo extends Component {//Рисуется карточка поста
    constructor(props) {
        super(props);
        this.state = {
            tags: this.props
        }
    }
    render() {
        const tags = this.props.tags.map((tag, index) => <p className="teg" key={index}>{tag}</p>);
        return (
            <div className="card-min">
                    <Link to={`/posts/${this.props.id}`}>
                        <img className='card-min-img' src={this.props.preview} alt=""/>
                    </Link>
                <div className="card-min-description">
                    <h3>{this.props.name}</h3>
                    <p>{this.props.description}</p>
                    <div className="card-min-description-tegs">
                        {tags}
                    </div>
                </div>
            </div>
        );
    }
}
export default PostMinInfo;
