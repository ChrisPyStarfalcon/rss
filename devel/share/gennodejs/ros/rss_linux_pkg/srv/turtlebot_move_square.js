// Auto-generated. Do not edit!

// (in-package rss_linux_pkg.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class turtlebot_move_squareRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sideLength = null;
      this.repetitions = null;
    }
    else {
      if (initObj.hasOwnProperty('sideLength')) {
        this.sideLength = initObj.sideLength
      }
      else {
        this.sideLength = 0.0;
      }
      if (initObj.hasOwnProperty('repetitions')) {
        this.repetitions = initObj.repetitions
      }
      else {
        this.repetitions = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type turtlebot_move_squareRequest
    // Serialize message field [sideLength]
    bufferOffset = _serializer.float64(obj.sideLength, buffer, bufferOffset);
    // Serialize message field [repetitions]
    bufferOffset = _serializer.int32(obj.repetitions, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type turtlebot_move_squareRequest
    let len;
    let data = new turtlebot_move_squareRequest(null);
    // Deserialize message field [sideLength]
    data.sideLength = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [repetitions]
    data.repetitions = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'rss_linux_pkg/turtlebot_move_squareRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bd481db479ec99c64e28864d3a771600';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 sideLength
    int32 repetitions
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new turtlebot_move_squareRequest(null);
    if (msg.sideLength !== undefined) {
      resolved.sideLength = msg.sideLength;
    }
    else {
      resolved.sideLength = 0.0
    }

    if (msg.repetitions !== undefined) {
      resolved.repetitions = msg.repetitions;
    }
    else {
      resolved.repetitions = 0
    }

    return resolved;
    }
};

class turtlebot_move_squareResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type turtlebot_move_squareResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type turtlebot_move_squareResponse
    let len;
    let data = new turtlebot_move_squareResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'rss_linux_pkg/turtlebot_move_squareResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new turtlebot_move_squareResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: turtlebot_move_squareRequest,
  Response: turtlebot_move_squareResponse,
  md5sum() { return '774421ec0e986291577c56de248181db'; },
  datatype() { return 'rss_linux_pkg/turtlebot_move_square'; }
};
