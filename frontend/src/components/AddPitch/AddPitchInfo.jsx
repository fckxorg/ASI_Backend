import React, {Component} from 'react';

class AddPitchInfo extends Component {
    render() {
        const dontReload = function(e){
            e.preventDefault();
            let name = document.getElementById('name').value;
            let description = document.getElementById('description').value;
            let preview = document.getElementById('preview').value;
            let video = document.getElementById('video').value;
            let necessary_investitions = document.getElementById('necessary_investitions').value;
            const data = {
                name:name,
                description:description,
                preview:preview,
                video:video,
                necessary_investitions:necessary_investitions
            };
            fetch('/pitch/add/',{
                method:'POST',
                mode: 'cors',
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => console.log(data))

            Array.prototype.forEach.call(document.getElementsByClassName('add-post-input'), function (input) {
                input.value = '';
            });
            alert('Проект добавлен')
        }
        return (
            <form method="post">
                <div className="add">
                    <h2>Создать пост</h2>
                    <div className="add-post">
                        <p className="add-post-p">Название</p>
                        <input className="add-post-input" type="text" placeholder="Название" id="name"/>
                    </div>
                    <div className="add-post">
                        <p className="add-post-p">Описание проекта</p>
                        <textarea className="add-post-input" type="text" placeholder="Описание проекта" rows="5"
                                  id="description"></textarea>
                    </div>
                    <div className="add-post">
                        <p className="add-post-p">URL картинки питча</p>
                        <input className="add-post-input" type="url" placeholder="URL картинки питча" id="preview"/>
                    </div>
                    <div className="add-post">
                        <p className="add-post-p">URL видео питча</p>
                        <input className="add-post-input" type="url" placeholder="URL видео питча" id="video"/>
                    </div>
                    <div className="add-post">
                        <p className="add-post-p">Сумма нужных инвестиций ₽</p>
                        <input className="add-post-input" type="number" placeholder="Количество нужных инвестиций ₽"
                               min="0" step="100" id="necessary_investitions"/>
                    </div>
                    <input className="add-post-btn" type='submit' value="Создать" onClick={dontReload}/>
                </div>
            </form>
        );
    }
}

export default AddPitchInfo;
