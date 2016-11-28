71 Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

思路：用栈存储，遇到".."出栈，"."或""不操作，其他入栈