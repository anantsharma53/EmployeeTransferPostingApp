import React from "react";
import { useState, useEffect } from 'react';
import './ActionPage2.css'
function ActionPage2() {
    const [post, setPost] = useState();
    const [employee, setEmployee] = useState();
    const [newemployee, setNewemployee] = useState();
    const [error, setError] = useState();
    
    function OnHandelSubmit(props) {
        console.log(props)

        fetch("http://127.0.0.1:8000/api/employee/search/?query=" + props)
            .then((res) => res.json())
            .then((jsonResponse) => {
                setEmployee(jsonResponse);
                // console.log(employee)  
                setError();
            })
            .catch((err) => {
                console.log(err);
                setError(err);
            })

    }
    function OnHandelRandomBlockSubmit(props) {
        console.log(props)
   
        // fetch("http://127.0.0.1:8000/api/employee/search/new?query=" + props)
        fetch("http://127.0.0.1:8000/api/employee/search/new?query="+props)
            .then((res) => res.json())
            .then((jsonResponse) => {
                setNewemployee(jsonResponse);
                // console.log(employee)  
                setError();
                {alert("Assigne Block and District")}
            })
            .catch((err) => {
                console.log(err);
                setError(err);
            })

    }
    function OnHandelRandomSubmit() {
        console.log()

        fetch("http://127.0.0.1:8000/api/employee/newoffice/")
            .then((res) => res.json())
            .then((jsonResponse) => {
                setNewemployee(jsonResponse);
                // console.log(employee)  
                setError();
            })
            .catch((err) => {
                console.log(err);
                setError(err);
            })

     }
    function OnHandelResetSubmit(){
        fetch("http://127.0.0.1:8000/api/employee/search/new?query=clean")
        fetch("http://127.0.0.1:8000/api/employee/clean/?query=clean")
            .then((res) => res.json())
            .then((jsonResponse) => {
                setNewemployee(jsonResponse);
                
                // console.log(employee)  
                setError();
            })
            .catch((err) => {
                console.log(err);
                setError(err);
            })
    }
    

    return (
        <>
            <div className='postSelection'>
                <div>
                    <label for="pet-select">Select Post:
                    </label>
                </div>
                <div>
                    <select id="select_box" value={post} onChange={e => setPost(e.target.value)}>
                        <option value="" selected="selected">--Please choose an option--</option>
                        <option value="OS">OS</option>
                        <option value="HC">HC</option>
                        <option value="LDC">LDC</option>
                        <option value="UDC">UDC</option>
                    </select>
                </div>
                <div>
                    <h4>{post}</h4>
                </div>
                <div>
                    <button type="button" class="btn btn-primary btn-block mb-4" onClick={() => OnHandelSubmit(post)} >View employee</button>
                </div>
            </div>
            <div className='tableDesigne'>
                <table>
                    <thead>
                        <tr>
                            <th>GPF No</th>
                            <th>Name</th>
                            <th>Designation</th>
                            <th>Current Office</th>
                            <th>Current Block</th>
                            <th>Current Posting Year</th>
                            <th>First Prev Office</th>
                            <th>First Prev Office Block</th>
                            <th>Second Prev Office</th>
                            <th>Second Prev Office Block</th>
                            <th>Dept Office</th>
                            <th>Dept Block</th>
                            <th>Alloted Office</th>
                            <th>Alloted Block</th>
                        </tr>
                    </thead>
                    <tbody>
                        {employee
                            &&
                            employee.map((employee, index) => (
                                <tr key={index}>
                                    <td>{employee.GPF_No}</td>
                                    <td>{employee.Name}</td>
                                    <td>{employee.Designation}</td>
                                    <td>{employee.Curr_office}</td>
                                    <td>{employee.Curr_block}</td>
                                    <td>{employee.Curr_post_year}</td>
                                    <td>{employee.First_post_office}</td>
                                    <td>{employee.First_post_office_block}</td>
                                    <td>{employee.Second_post_office}</td>
                                    <td>{employee.Second_post_office_block}</td>
                                    <td>{employee.Dept_office}</td>
                                    <td>{employee.Dept_block}</td>
                                    <td>Wait..</td>
                                    <td>Wait..</td>
                                </tr>
                            ))}
                    </tbody>
                </table>
            </div>
            <div className='Actionbutton'>
            
                <button class="favorite styled" onClick={() => OnHandelRandomBlockSubmit(post)}type="button">
                    Click to Assigne Block and District 
                    </button>
                 <button class="favorite styled" onClick={() => OnHandelRandomSubmit()}
                    type="button">
                    Click to Assigne Office
                </button>
               <button class="favorite styled" onClick={() => OnHandelResetSubmit()}

                    type="button">
                    Click to Clear Assigne Office
                </button>
                {/* <button type="button" onClick={() => Rset()}>
                    Reload Page
                </button> */}
            </div>
            <div class="p-3 text-center bg-light">
                <h3 class="mb-3">New Employee List </h3>

            </div>
            <>
                <div className='tableDesigne'>
                    <table>
                        <thead>
                            <tr>
                                <th>GPF No</th>
                                <th>Name</th>
                                <th>Designation</th>
                                <th>Current Office</th>
                                <th>Current Block</th>
                                <th>Current Posting Year</th>
                                <th>First Prev Office</th>
                                <th>First Prev Office Block</th>
                                <th>Second Prev Office</th>
                                <th>Second Prev Office Block</th>
                                <th>Dept Office</th>
                                <th>Dept Block</th>
                                <th>Alloted Office</th>
                                <th>Alloted Block</th>
                            </tr>
                        </thead>
                        <tbody>
                            {newemployee
                                &&
                                newemployee.map((newemployee, index) => (
                                    <tr key={index}>
                                        <td>{newemployee.GPF_No}</td>
                                        <td>{newemployee.Name}</td>
                                        <td>{newemployee.Designation}</td>
                                        <td>{newemployee.Curr_office}</td>
                                        <td>{newemployee.Curr_block}</td>
                                        <td>{newemployee.Curr_post_year}</td>
                                        <td>{newemployee.First_post_office}</td>
                                        <td>{newemployee.First_post_office_block}</td>
                                        <td>{newemployee.Second_post_office}</td>
                                        <td>{newemployee.Second_post_office_block}</td>
                                        <td>{newemployee.Dept_office}</td>
                                        <td>{newemployee.Dept_block}</td>
                                        <td>{newemployee.Alloted_office}</td>
                                        <td>{newemployee.Alloted_Block}</td>

                                    </tr>
                                ))}
                        </tbody>
                    </table>
                </div>
            </>

        </>
    );

}

export default ActionPage2;