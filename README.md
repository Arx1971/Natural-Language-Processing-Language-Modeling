<h1> Natural Language Processing</h1>
<h2>Objective: </h2>
<ul>
	<li>Train Several Language Models</li>
	<li>Evaluate them on two test corpora</li>
</ul>
<h2>Pre-Porcessing training Corpora</h2>
<ul>
	<li>Pad each sentence in the training and test corpora with start and end symbols (you can
		use <s> and </s>, respectively).</li>
	<li>Lowercase all words in the training and test corpora. Note that the data already has
		been tokenized (i.e. the punctuation has been split off words).</li>
	<li>
		Replace all words occurring in the training data once with the token <unk>. Every word
		in the test data not seen in training should be treated as <unk>.
	</li>
</ul>