# movie.tcl
# To run, in the vmd tckon type: 'source movie.tcl'

# Script requires TopoTools and pbctools

package require topotools
package require pbctools

#set molid [topo readlammpsdata in.lammpstrj]
mol new output_difusion.lammpstrj
#mol addfile in.dcd


# Set the representation, delete the initial representation
# created by vmd

mol delrep 0 top
mol representation VDW 0.4 10.0
mol color Type
mol selection {all}
mol material EdgyShiny
mol addrep top

# Set the scene: adjust display height
# and rotate axes a bit, set the background
# to white

display height 5
# rotate x by -45; rotate y by 45; rotate z by 45
rotate z by -90; rotate x by -45
translate to 0 0.5 0

proc box_molecule {molid} {
      # get the min and max values for each of the directions
      # (I'm not sure if this is the best way ... )
      set sel [atomselect top all]

      #set coords [lsort -real [$sel get x]]
      #set minx [lindex $coords 0]
      #set maxx [lindex [lsort -real -decreasing $coords] 0]

      #set coords [lsort -real [$sel get y]]
      #set miny [lindex $coords 0]
      #set maxy [lindex [lsort -real -decreasing $coords] 0]

      #set coords [lsort -real [$sel get z]]
      #set minz [lindex $coords 0]
      #set maxz [lindex [lsort -real -decreasing $coords] 0]


      set minx 20
      set maxx 20.12

      set miny 9
      set maxy 11

      set minz 0
      set maxz 0.5

      # and draw the lines
      draw materials off
      draw color yellow
      draw line "$minx $miny $minz" "$maxx $miny $minz"
      draw line "$minx $miny $minz" "$minx $maxy $minz"
      draw line "$minx $miny $minz" "$minx $miny $maxz"

      draw line "$maxx $miny $minz" "$maxx $maxy $minz"
      draw line "$maxx $miny $minz" "$maxx $miny $maxz"

      draw line "$minx $maxy $minz" "$maxx $maxy $minz"
      draw line "$minx $maxy $minz" "$minx $maxy $maxz"

      draw line "$minx $miny $maxz" "$maxx $miny $maxz"
      draw line "$minx $miny $maxz" "$minx $maxy $maxz"

      draw line "$maxx $maxy $maxz" "$maxx $maxy $minz"
      draw line "$maxx $maxy $maxz" "$minx $maxy $maxz"
      draw line "$maxx $maxy $maxz" "$maxx $miny $maxz"
}

box_molecule top

# miny=9
# maxy=11

# set sel [atomselect top all]
# draw color yellow
# draw line "20 $miny  0" "20 $maxy 0.5"

pbc box

#set nframes [molinfo $molid get numframes]
#set nframes 100

#for {set i 1} {$i < $nframes} {incr i} {
#render TachyonInternal\
#[format “snap-03.%05
#d.tga" $i]
#}
