LOAD COPY
     FROM copy:/tmp/cdr-csv/Master.csv.*
          (
            customer_id,
            customer_ip,
            uuid,
            caller_id_number,
            destination_number,
            chan_name,
            start_stamp,
            answered_stamp null if blanks,
            end_stamp,
            duration,
            read_codec,
            write_codec,
            hangup_cause,
            hangup_cause_q850,
            gateway_id null if blanks,
            cost_rate,
            prefix,
            country,
            rate,
            init_block,
            block_min_duration,
            lcr_carrier_id_id null if blanks,
            ratecard_id_id null if blanks,
            lcr_group_id_id null if blanks,
            sip_user_agent,
            sip_rtp_rxstat,
            sip_rtp_txstat,
            bleg_uuid,
            switchname,
            switch_ipv4,
            hangup_disposition,
            effectiv_duration,
            sip_hangup_cause,
            effective_duration,
            billsec,
            total_sell,
            total_cost,
            sell_destination,
            cost_destination,
            customerdirectory_id
         )
    INTO postgresql:///pgloader
    TARGET TABLE cdr
    WITH
      fields escaped by double-quote,
      fields terminated by ','

    SET work_mem to '14MB',
        standard_conforming_strings to 'on'
