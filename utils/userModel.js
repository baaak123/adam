const mongoose = require('mongoose')

// Define Schemes
const userSchema = new mongoose.Schema({
    username: { type: String },
    email: { type: String },
    phone: { type: String } , 
    password:{type : String}
  },
  {
    timestamps: true
  });

  // Create Model & Export
  module.exports = mongoose.model('User', userSchema);