
(cl:in-package :asdf)

(defsystem "rss_linux_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "turtlebot_move_square" :depends-on ("_package_turtlebot_move_square"))
    (:file "_package_turtlebot_move_square" :depends-on ("_package"))
  ))