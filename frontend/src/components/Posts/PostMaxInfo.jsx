import React, {Component} from 'react';

class PostMaxInfo extends Component {
    render() {
        const tags = this.props.tags.map(tag => <p className="teg">{tag}</p>)
        return (
            <div className="post-info">
                <div className="card-max">

                    <div className="video">
                        <video controls="controls" poster={this.props.preview}>
                            <source src={this.props.video}/>
                        </video>
                        <div className="card-max-description-tegs-under-video">
                            {tags}
                        </div>
                    </div>
                    <div className="card-max-description">
                        <h1 className="card-max-description-h1">{this.props.name}</h1>
                        <p className="card-max-description-p">{this.props.description}</p><br/>
                        <p className="card-max-description-p"><h1><b>{this.props.necessary_investitions} ₽</b></h1></p>
                        <button className="card-max-description-btn-yellow">Отслеживать</button>
                        <button className="card-max-description-btn">Инвестировать</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default PostMaxInfo;
