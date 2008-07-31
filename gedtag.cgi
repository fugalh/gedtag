#!/usr/bin/ruby

require 'cgi'
require 'pathname'

cgi = CGI.new

IO.popen('/usr/bin/ruby -T gedtag', 'w+') {|f|
  f.puts cgi['gedcom'].read
  f.close_write

  p = Pathname.new cgi['gedcom'].original_filename
  cgi.out('type' => 'application/x-gedcom',
	  'Content-Disposition' => "attachment; filename=#{p.basename}") {
    f.read
  }
}
