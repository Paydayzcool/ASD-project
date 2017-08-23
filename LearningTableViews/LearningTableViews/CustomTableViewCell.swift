//
//  CustomTableViewCell.swift
//  LearningTableViews
//
//  Created by Callum Koh on 23/8/17.
//  Copyright © 2017 pop("Goes the weasel"). All rights reserved.
//

import UIKit

class CustomTableViewCell: UITableViewCell {

    @IBOutlet weak var label: UILabel!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
