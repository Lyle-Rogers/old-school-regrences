import React from 'react';
import { NavLink } from 'react-router-dom';

export default function() {
    return (
        <div>
            <div>
                <NavLink exact to="/discussion">Discussion</NavLink>                                   
            </div>

            <div>
                <NavLink exact to="/rules">Rules</NavLink>                                  
            </div>

            <div>
                <NavLink exact to="/workflow">Workflow</NavLink>              
            </div>
        </div>
    );
}