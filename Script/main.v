`timescale 1ns / 1ps

module main(
    output MR, MY, MG,
    output SR, SY, SG,
    output ST,          
    input reset,
    input C,
    input Emergency,    
    input Clk
);

    // Memanggil modul Traffic
    traffic traffic_system(
        .MR(MR), .MY(MY), .MG(MG), 
        .SR(SR), .SY(SY), .SG(SG), 
        .ST(ST),
        .reset(reset), 
        .C(C), 
        .Emergency(Emergency), 
        .Clk(Clk)
    );

endmodule
