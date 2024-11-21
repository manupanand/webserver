"use strict";
//user controller
Object.defineProperty(exports, "__esModule", { value: true });
exports.createUser = exports.getUsers = void 0;
const getUsers = (req, res) => {
    res.status(200).json({
        message: `got user`
    });
};
exports.getUsers = getUsers;
const createUser = (req, res) => {
    const { name, email } = req.body;
    res.status(200).json({
        message: `User created`,
        name: `${name}`,
        email: `${email}`
    });
};
exports.createUser = createUser;
