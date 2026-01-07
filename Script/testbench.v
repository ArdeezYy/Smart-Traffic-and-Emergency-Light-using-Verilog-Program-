`timescale 1ns / 1ps

module testbench;

    // Outputs
    wire MR, MY, MG, SR, SY, SG, ST;
    
    // Inputs
    reg C, reset, Clk, Emergency;

    // Instantiate MAIN (Unit Paling Atas)
    main uut (
        .MR(MR), .MY(MY), .MG(MG), 
        .SR(SR), .SY(SY), .SG(SG), 
        .ST(ST),
        .reset(reset), 
        .C(C), 
        .Emergency(Emergency),
        .Clk(Clk)
    );

    initial begin
        // Inisialisasi
        C = 0;
        reset = 1;
        Emergency = 0;
        Clk = 0;

        // Reset selesai
        #50; reset = 0; 
        
        // --- NORMAL MODE ---
        C = 1;
        #700; 
        
        // --- EMERGENCY MODE ---
        $display("EMERGENCY ON");
        Emergency = 1;
        #400; // Lampu harus hijau terus disini
        
        // Matikan
        Emergency = 0;
        $display("EMERGENCY OFF");

        // --- NORMAL LAGI ---
        #400;
        
        $stop;
    end

    always begin
        #50 Clk = ~Clk;
    end
endmodule
