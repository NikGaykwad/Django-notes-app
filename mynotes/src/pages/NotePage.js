import React, { useEffect, useState } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'

const NotePage = () => {
  let { id } = useParams()
  let navigate = useNavigate()
  let [note, setNote] = useState({ body: "" })

  useEffect(() => {
    let getNote = async () => {
      if (id === 'new') return
      let response = await fetch(`/api/notes/${id}/`)
      let data = await response.json()
      setNote(data)
    }
    getNote()
  }, [id])

  const createNote = async () => {
    await fetch(`/api/notes/create/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        body: note.body,
      }),
    })
  }

  const updateNote = async () => {
    await fetch(`/api/notes/${id}/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        body: note.body,
      }),
    })
  }

  const deleteNote = async () => {
    await fetch(`/api/notes/${id}/delete/`, {
      method: 'DELETE',
    })
    navigate('/')
  }

  const handleSubmit = async () => {
    if (id === 'new' && note.body.trim() !== "") {
      await createNote()
    } else if (id !== 'new' && note.body.trim() !== "") {
      await updateNote()
    } else if (id !== 'new' && note.body.trim() === "") {
      await deleteNote()
    }
    navigate('/')
  }

  return (
    <div className='note'>
      <div className="note-header">
        <h3>
          <Link to='/'>
            <ArrowLeft onClick={handleSubmit} />
          </Link>
        </h3>
        {id !== 'new' ? (
          <button onClick={deleteNote}>Delete</button>
        ) : (
          <button onClick={handleSubmit}>Save</button>
        )}
      </div>

      <div className="note-body">
        <textarea
          value={note.body}
          onChange={(e) => setNote({ ...note, body: e.target.value })}
        />
      </div>
    </div>
  )
}

export default NotePage

