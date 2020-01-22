//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package test2.simulations;
//
// TODO documentation
//
import test2.Source;
import test2.Sink;
import test2.LoadBalancer;
network Network
{
    @display("bgb=384,312");
    submodules:
        A: Source {
            @display("p=187,27");
        }
        B: LoadBalancer {
            @display("p=187,120");
        }
        D: Sink {
            @display("p=273,228");
        }
        C: Sink {
            @display("p=108,228");
        }
    connections:
        A.out --> B.in;
        B.out[0] --> C.in;
        B.out[1] --> D.in;
}

