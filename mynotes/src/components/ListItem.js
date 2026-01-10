import React from 'react'
import { Link } from "react-router-dom";

let safeBody = (note) => {
    return note.body ? note.body : ""
}

let getTitle = (note) => {
    let body = safeBody(note)
    let title = body.split('\n')[0]

    if (title.length > 25) {
        title = title.slice(0, 25) + '...'
    }
    return title || "Untitled"
}

let getDate = (note) => {
    return new Date(note.updated).toLocaleDateString()
}

let getContent = (note) => {
    let body = safeBody(note)
    let title = body.split('\n')[0]
    let content = body.replace(title, "")

    if (content.length > 69) {
        return content.slice(0, 69) + '...'
    }
    return content || "No content"
}

const ListItem = ({ note }) => {
    return (
        <div className='notes-list-item'>
            <Link to={`/note/${note.id}`}>
                <h3>{getTitle(note)}</h3>
                <p>{getContent(note)}</p>
                <p>{getDate(note)}</p>
            </Link>
        </div>
    )
}

export default ListItem

