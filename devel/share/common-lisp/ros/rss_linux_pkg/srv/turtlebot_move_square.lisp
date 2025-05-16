; Auto-generated. Do not edit!


(cl:in-package rss_linux_pkg-srv)


;//! \htmlinclude turtlebot_move_square-request.msg.html

(cl:defclass <turtlebot_move_square-request> (roslisp-msg-protocol:ros-message)
  ((sideLength
    :reader sideLength
    :initarg :sideLength
    :type cl:float
    :initform 0.0)
   (repetitions
    :reader repetitions
    :initarg :repetitions
    :type cl:integer
    :initform 0))
)

(cl:defclass turtlebot_move_square-request (<turtlebot_move_square-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <turtlebot_move_square-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'turtlebot_move_square-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rss_linux_pkg-srv:<turtlebot_move_square-request> is deprecated: use rss_linux_pkg-srv:turtlebot_move_square-request instead.")))

(cl:ensure-generic-function 'sideLength-val :lambda-list '(m))
(cl:defmethod sideLength-val ((m <turtlebot_move_square-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss_linux_pkg-srv:sideLength-val is deprecated.  Use rss_linux_pkg-srv:sideLength instead.")
  (sideLength m))

(cl:ensure-generic-function 'repetitions-val :lambda-list '(m))
(cl:defmethod repetitions-val ((m <turtlebot_move_square-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss_linux_pkg-srv:repetitions-val is deprecated.  Use rss_linux_pkg-srv:repetitions instead.")
  (repetitions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <turtlebot_move_square-request>) ostream)
  "Serializes a message object of type '<turtlebot_move_square-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'sideLength))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'repetitions)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <turtlebot_move_square-request>) istream)
  "Deserializes a message object of type '<turtlebot_move_square-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sideLength) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'repetitions) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<turtlebot_move_square-request>)))
  "Returns string type for a service object of type '<turtlebot_move_square-request>"
  "rss_linux_pkg/turtlebot_move_squareRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtlebot_move_square-request)))
  "Returns string type for a service object of type 'turtlebot_move_square-request"
  "rss_linux_pkg/turtlebot_move_squareRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<turtlebot_move_square-request>)))
  "Returns md5sum for a message object of type '<turtlebot_move_square-request>"
  "774421ec0e986291577c56de248181db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'turtlebot_move_square-request)))
  "Returns md5sum for a message object of type 'turtlebot_move_square-request"
  "774421ec0e986291577c56de248181db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<turtlebot_move_square-request>)))
  "Returns full string definition for message of type '<turtlebot_move_square-request>"
  (cl:format cl:nil "float64 sideLength~%int32 repetitions~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'turtlebot_move_square-request)))
  "Returns full string definition for message of type 'turtlebot_move_square-request"
  (cl:format cl:nil "float64 sideLength~%int32 repetitions~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <turtlebot_move_square-request>))
  (cl:+ 0
     8
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <turtlebot_move_square-request>))
  "Converts a ROS message object to a list"
  (cl:list 'turtlebot_move_square-request
    (cl:cons ':sideLength (sideLength msg))
    (cl:cons ':repetitions (repetitions msg))
))
;//! \htmlinclude turtlebot_move_square-response.msg.html

(cl:defclass <turtlebot_move_square-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass turtlebot_move_square-response (<turtlebot_move_square-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <turtlebot_move_square-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'turtlebot_move_square-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rss_linux_pkg-srv:<turtlebot_move_square-response> is deprecated: use rss_linux_pkg-srv:turtlebot_move_square-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <turtlebot_move_square-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss_linux_pkg-srv:success-val is deprecated.  Use rss_linux_pkg-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <turtlebot_move_square-response>) ostream)
  "Serializes a message object of type '<turtlebot_move_square-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <turtlebot_move_square-response>) istream)
  "Deserializes a message object of type '<turtlebot_move_square-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<turtlebot_move_square-response>)))
  "Returns string type for a service object of type '<turtlebot_move_square-response>"
  "rss_linux_pkg/turtlebot_move_squareResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtlebot_move_square-response)))
  "Returns string type for a service object of type 'turtlebot_move_square-response"
  "rss_linux_pkg/turtlebot_move_squareResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<turtlebot_move_square-response>)))
  "Returns md5sum for a message object of type '<turtlebot_move_square-response>"
  "774421ec0e986291577c56de248181db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'turtlebot_move_square-response)))
  "Returns md5sum for a message object of type 'turtlebot_move_square-response"
  "774421ec0e986291577c56de248181db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<turtlebot_move_square-response>)))
  "Returns full string definition for message of type '<turtlebot_move_square-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'turtlebot_move_square-response)))
  "Returns full string definition for message of type 'turtlebot_move_square-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <turtlebot_move_square-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <turtlebot_move_square-response>))
  "Converts a ROS message object to a list"
  (cl:list 'turtlebot_move_square-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'turtlebot_move_square)))
  'turtlebot_move_square-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'turtlebot_move_square)))
  'turtlebot_move_square-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'turtlebot_move_square)))
  "Returns string type for a service object of type '<turtlebot_move_square>"
  "rss_linux_pkg/turtlebot_move_square")