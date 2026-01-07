`timescale 1ns / 1ps

module timer(
    output TS,     
    output TL,     
    input ST,      
    input Clk
);

    // PARAMETER WAKTU
    parameter TIME_SMALL = 2;
    parameter TIME_LONG  = 4;

    reg [31:0] value = 0; 

    // Logika Output
    assign TS = (value >= TIME_SMALL);
    assign TL = (value >= TIME_LONG);

    // Logika Penghitung
    always @(posedge Clk) begin
        if (ST == 1) begin
            value <= 0;          // Reset hitungan
        end else begin
            value <= value + 1;  // Menghitung naik
        end
    end

endmodule
