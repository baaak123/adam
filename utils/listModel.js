const mongoose = require('mongoose')

// Define Schemes
const listSchema = new mongoose.Schema({
    title: { type: String },
    author: { type: String },
    desc: { type: String } 
  },
  {
    timestamps: true
  });

  // Create Model & Export
  module.exports = mongoose.model('List', listSchema);